#!/bin/bash
# setup_env.sh

ENV_YML="environment.yml"

# Conda 환경 생성
if [ -f "$ENV_YML" ]; then
  echo "environment.yml file found. Creating Conda environment..."
  conda env create -f $ENV_YML
  if [ $? -eq 0 ]; then
    echo "Conda environment created successfully."
  else
    echo "Failed to create Conda environment. Check the environment.yml file for errors."
    exit 1
  fi
else
  echo "No environment.yml file found. Skipping Conda environment creation."
fi

# Conda 환경 활성화
ENV_NAME=$(head -n 1 $ENV_YML | cut -d ' ' -f 2)
if [ -n "$ENV_NAME" ]; then
  echo "Activating Conda environment: $ENV_NAME"
  conda activate $ENV_NAME
  if [ $? -eq 0 ]; then
    echo "Conda environment '$ENV_NAME' activated successfully."
  else
    echo "Failed to activate Conda environment '$ENV_NAME'."
  fi
else
  echo "Unable to determine environment name from environment.yml. Skipping activation."
fi
