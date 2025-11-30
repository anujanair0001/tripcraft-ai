"""
Setup script for TripCraft AI
Built with AI Agent Development Kit (ADK)
"""

from setuptools import setup, find_packages

setup(
    name="tripcraft-ai",
    version="1.0.0",
    description="Context-Aware Multi-Agent System for Personalized Travel Planning & Budget Optimization",
    long_description=open("../README.md").read(),
    long_description_content_type="text/markdown",
    author="AI Agent Development Course",
    packages=find_packages(),
    python_requires=">=3.7",
    install_requires=[
        # AI Agent Development Kit
        "amazon-adk>=1.0.0",
        
        # Core dependencies
        "google-generativeai>=0.3.0",
        "pandas>=1.5.0",
        "numpy>=1.24.0",
        "python-dotenv>=1.0.0",
        "pydantic>=2.0.0",
        
        # Utilities
        "requests>=2.28.0",
        "typing-extensions>=4.5.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "black>=23.0.0",
            "flake8>=6.0.0",
        ]
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Education",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    entry_points={
        "console_scripts": [
            "tripcraft-ai=main:run_demo",
        ],
    },
)