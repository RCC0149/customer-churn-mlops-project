#!/bin/bash
set -e

# Paths
MODEL_DIR=~/sagemaker-studiolab-notebooks/telco-customer-churn-pred/app/models
S3_PATH=s3://telco-churn-data-rcc/models/model.tar.gz

cd $MODEL_DIR

# Clean up old tarball
rm -f model.tar.gz

# Create tarball without .ipynb_checkpoints
tar --exclude='code/.ipynb_checkpoints' -czf model.tar.gz \
    churn_model.pkl scaler.pkl code/

echo "✅ model.tar.gz built."

# Upload to S3
aws s3 cp model.tar.gz $S3_PATH

echo "✅ model.tar.gz uploaded to $S3_PATH"

# Verify upload
echo "🔍 Verifying upload in S3..."
aws s3 ls $S3_PATH

# Make it executable, and run it.
# chmod +x rebuild_model.sh# ./rebuild_model.sh

