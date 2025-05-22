from extract import (
    convert_pdf_to_images,
    extract_text_from_images,
    extract_text_from_pdf,
)
from metrics import init_db, insert_metrics
from metrics_openai import extract_metrics_with_openai
from rag_pipeline import create_chunks, create_vector_store


def process_pdf(pdf_path):
    print("Converting PDF to text...")
    images = convert_pdf_to_images(pdf_path)
    img_text = extract_text_from_images(images)
    pdf_text = extract_text_from_pdf(pdf_path)
    full_text = pdf_text + "\n\n" + img_text

    print("Initializing DB and storing metrics...")
    init_db()
    metrics = extract_metrics_with_openai(full_text)
    insert_metrics(metrics)

    print("Creating vector store for RAG...")
    chunks = create_chunks(full_text)
    create_vector_store(chunks)

    print("Processing complete!")


if __name__ == "__main__":
    process_pdf("Q1FY24.pdf")
