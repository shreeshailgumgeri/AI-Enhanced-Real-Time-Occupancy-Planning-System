from setuptools import setup, find_packages

setup(
    name="AI-Enhanced-Real-Time-Occupancy-Planning-System",
    version="0.1.0",
    description="A Natural Language Interface for Occupancy Query System integrating VergeSense sensor data with AI models.",
    author="Your Name",
    author_email="your.email@example.com",
    url="https://github.com/yourusername/vergesense-nlp-query",
    packages=find_packages(where="app"),
    package_dir={"": "app"},
    install_requires=[
        "fastapi",
        "uvicorn",
        "sqlalchemy",
        "pydantic",
        "requests",
        "openai",
        "anthropic",
        "python-dotenv"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Framework :: FastAPI",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)