import os

# Example configuration.
# Secrets should come from environment variables or a secret manager.

AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")

DB_PASSWORD = os.getenv("DB_PASSWORD")

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

STRIPE_API_KEY = os.getenv("STRIPE_API_KEY")
