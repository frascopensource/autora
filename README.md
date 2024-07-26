# Autora
<p align="center">
  <img src="https://github.com/user-attachments/assets/512e940f-e5bf-41e1-8bf0-87e55a6d6e3d" />
</p>

Autora is a collection of scripts designed to assist town halls in disseminating information to citizens efficiently and effectively.

## Table of Contents

- [Autora](#autora)
  - [Table of Contents](#table-of-contents)
  - [Features](#features)
  - [Installation](#installation)
  - [Usage](#usage)

## Features

- Automates the distribution of information
- Highly customizable

## Installation

To install Autora, you can use the provided `Makefile` for setting up the environment and dependencies. Follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/frascopensource/autora.git
    ```
2. Navigate to the project directory:
    ```bash
    cd autora
    ```
3. Install the required dependencies:
    ```bash
    make install
    ```

## Usage

To start using Autora, follow these steps:

1. Ensure you have completed the installation steps.
2. Create a configuration file based on `example.env`:
    ```bash
    cp example.env .env
    ```
3. Run the application:
    ```bash
    make run
    ```

For other available commands, you can check the `Makefile` by running:
```bash
make help
