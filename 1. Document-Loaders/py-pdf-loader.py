from langchain_community.document_loaders import PyPDFLoader

loader=PyPDFLoader('dl-curriculum.pdf')

docs=loader.load()

print(len(docs))