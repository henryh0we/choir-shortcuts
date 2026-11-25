"""Remove PDF annotations from Library.zip. Requires pypdf."""

from io import BytesIO
from pathlib import Path, PurePosixPath
from tempfile import TemporaryDirectory
from zipfile import ZipFile

from pypdf import PdfReader, PdfWriter


def main():
    workspace = Path(__file__).resolve().parent
    output = workspace / "Library-clean"
    if output.exists():
        raise SystemExit(f"{output} already exists. Rename it before rerunning.")

    scores = changed = removed = 0
    with ZipFile(workspace / "Library.zip") as archive, TemporaryDirectory(
        dir=workspace
    ) as temporary:
        staging = Path(temporary) / output.name
        for entry in archive.infolist():
            path = PurePosixPath(entry.filename)
            if entry.is_dir() or path.parts[:1] != ("Library",) or path.suffix.lower() != ".pdf":
                continue
            if (
                any(part.rstrip(" .") != part for part in path.parts)
                or "\\" in entry.filename
                or ":" in entry.filename
            ):
                raise ValueError(f"Unsafe ZIP path: {entry.filename}")

            destination = staging.joinpath(*path.parts[1:])
            if destination.exists():
                destination = destination.parent / "Alternate versions" / path.name
                print(f"Kept both versions: {destination.relative_to(staging)}")
            data = archive.read(entry)
            reader = PdfReader(BytesIO(data))
            annotations = sum(
                len(page["/Annots"]) for page in reader.pages if "/Annots" in page
            )
            destination.parent.mkdir(parents=True, exist_ok=True)
            with destination.open("xb") as file:
                if annotations:
                    writer = PdfWriter(clone_from=reader)
                    writer.remove_annotations(subtypes=None)
                    writer.write(file)
                else:
                    file.write(data)

            if annotations:
                with destination.open("rb") as file:
                    cleaned = PdfReader(file)
                    if len(cleaned.pages) != len(reader.pages) or any(
                        len(page["/Annots"]) for page in cleaned.pages if "/Annots" in page
                    ):
                        raise ValueError(f"Could not verify cleaned PDF: {path}")
                changed += 1
                removed += annotations
            scores += 1

        if not scores:
            raise SystemExit("No PDFs found under Library/ in Library.zip.")
        staging.rename(output)
    print(f"Wrote {scores} PDFs to {output.name}. Removed {removed} annotations from {changed} PDFs.")


if __name__ == "__main__":
    main()
