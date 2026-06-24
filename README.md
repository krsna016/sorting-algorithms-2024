# sorting-algorithms-2024

[![Language: Python](https://img.shields.io/badge/language-Python-blue.svg)]()
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![CI Pipeline](https://github.com/krsna016/sorting-algorithms-2024/actions/workflows/ci.yml/badge.svg)](https://github.com/krsna016/sorting-algorithms-2024/actions/workflows/ci.yml)
[![Security: CodeQL](https://github.com/krsna016/sorting-algorithms-2024/actions/workflows/codeql.yml/badge.svg)](https://github.com/krsna016/sorting-algorithms-2024/actions/workflows/codeql.yml)

Professional engineering repository configurations deployed inside your GitHub profile.

---

## Overview & Core Description

This repository contains the implementation of various sorting algorithms in multiple programming languages like Python and Java. Sorting algorithms are fundamental in computer science and are used to arrange data in a particular order, usually ascending or descending.

## Table of Contents
- [About](#about)
- [List of Algorithms](#list-of-algorithms)
- [Getting Started](#getting-started)

## About
This repository provides a collection of popular sorting algorithms implemented in Java. Each algorithm is accompanied by an explanation of how it works, its time and space complexities, and best/worst-case scenarios. These implementations are great for students learning sorting algorithms, interview preparation, or anyone looking to deepen their understanding of algorithm design.

## List of Algorithms

### 1. **Bubble Sort**
- **Description**: A simple comparison-based algorithm that repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order.
- **Time Complexity**:
    - Best: O(n)
    - Average: O(n²)
    - Worst: O(n²)
- **Space Complexity**: O(1)

### 2. **Selection Sort**
- **Description**: Continuously selects the smallest element from the unsorted portion and swaps it with the element at the current position.
- **Time Complexity**:
    - Best: O(n²)
    - Average: O(n²)
    - Worst: O(n²)
- **Space Complexity**: O(1)

### 3. **Insertion Sort**
- **Description**: Builds a sorted array one element at a time by inserting each new element into its proper place among those already sorted.
- **Time Complexity**:
    - Best: O(n)
    - Average: O(n²)
    - Worst: O(n²)
- **Space Complexity**: O(1)

### 4. **Merge Sort**
- **Description**: A divide-and-conquer algorithm that divides the array into halves, recursively sorts them, and then merges the sorted halves.
- **Time Complexity**:
    - Best: O(n log n)
    - Average: O(n log n)
    - Worst: O(n log n)
- **Space Complexity**: O(n)

### 5. **Quick Sort**
- **Description**: A divide-and-conquer algorithm that picks a pivot, partitions the array around the pivot, and recursively sorts the partitions.
- **Time Complexity**:
    - Best: O(n log n)
    - Average: O(n log n)
    - Worst: O(n²)
- **Space Complexity**: O(log n)

### 6. **Heap Sort**
- **Description**: Utilizes a binary heap structure to sort an array by first building the heap and then repeatedly extracting the maximum element.
- **Time Complexity**:
    - Best: O(n log n)
    - Average: O(n log n)
    - Worst: O(n log n)
- **Space Complexity**: O(1)

### 7. **Counting Sort**
- **Description**: Counts the number of occurrences of each unique element, then calculates their positions in the sorted array.
- **Time Complexity**:
    - Best: O(n + k)
    - Average: O(n + k)
    - Worst: O(n + k)
- **Space Complexity**: O(n + k)

### 8. **Radix Sort**
- **Description**: Non-comparative sorting algorithm that sorts integers by processing digits.
- **Time Complexity**:
    - Best: O(nk)
    - Average: O(nk)
    - Worst: O(nk)
- **Space Complexity**: O(n + k)

### 9. **Shell Sort**
- **Description**: A generalization of insertion sort that allows exchanges of elements that are far apart.
- **Time Complexity**:
    - Best: O(n log n)
    - Average: O(n log² n)
    - Worst: O(n²)
- **Space Complexity**: O(1)

### 10. **Bucket Sort**
- **Description**: Distributes elements into several buckets, sorts the buckets, and then concatenates them.
- **Time Complexity**:
    - Best: O(n + k)
    - Average: O(n + k)
    - Worst: O(n²)
- **Space Complexity**: O(n + k)

## Getting Started

### Prerequisites
To run the algorithms in this repository, you'll need:
- **Java JDK 8+** (for Java implementations)

### Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/sorting-algorithms.git
   cd sorting-algorithms
   ```










---

## System Design & Folder Structure
```text
.github/                  # CI/CD pipelines, Dependabot, and Issue/PR schemas
.editorconfig             # Unified file formatting configuration
.gitattributes            # Normalization variables for LF line endings
.gitignore                # Local environment overrides and cache limits
.pre-commit-config.yaml   # Quality check execution triggers
LICENSE                   # Permissive open-source MIT License
Makefile                  # Development workspace orchestrator
CHANGELOG.md              # Historical version tracking
CONTRIBUTING.md           # Developer onboarding guidelines
CODE_OF_CONDUCT.md        # Communication guidelines
SECURITY.md               # Responsible vulnerability disclosures
```

---

## Tooling & Tech Stack
- **Primary Environment:** Python runtime.
- **Workflow Automation:** GitHub Actions CI, Dependabot, and CodeQL.
- **Standards Checkers:** Git `pre-commit` hook validations.

---

## Quickstart & Local Setup
1. Clone this repository locally:
   ```bash
   git clone https://github.com/krsna016/sorting-algorithms-2024.git
   cd sorting-algorithms-2024
   ```
2. Trigger the local setup runner:
   ```bash
   make help
   ```

---

## Security & Responsible Disclosure
For details on disclosing vulnerabilities or hardcoded secrets, refer directly to our [SECURITY.md](SECURITY.md) guidelines.

---

## License
This repository is licensed under the permissive **MIT License**. For details, see the [LICENSE](LICENSE) file.
