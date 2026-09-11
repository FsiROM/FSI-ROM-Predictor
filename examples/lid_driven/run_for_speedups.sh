#!/bin/bash

# Target directory
TARGET_DIR="./result_arrays/speedups/dt10/surrogate_proposed"

# Loop 10 times
for i in $(seq 1 10); do
    echo "Running iteration $i..."

    # Run the Python script
    zsh -c "source ~/.zshrc && /opt/homebrew/bin/python3 MainKratos.py"

    # Format run number with two digits (01, 02, ..., 10)
    RUN_ID=$(printf "%02d" "$i")

    # Rename folder
    mv coSimData "coSimData_${RUN_ID}"

    # Move to target directory
    mv "coSimData_${RUN_ID}" "$TARGET_DIR"

    echo "Iteration $i completed."
done

echo "All runs completed."
