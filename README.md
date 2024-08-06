<a id="readme-top"></a>

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/joaroque/wtf">
    <img src="https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExZGxzcmVvYXQ2bXZnc25ldnQyenpsNTlvbGplMDZ0cDRrejV1bGRkMCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/uHox9Jm5TyTPa/giphy.gif" alt="Logo" width="" height="">
  </a>

  <h3 align="center">WTF: What is The Fault?</h3>

  <p align="center">
   Inspired by The Fuck, WTF enhances functionality by offering detailed error explanations, making it a more streamlined and user-friendly alternative
    <br />
    <br />
    <a href="https://github.com/joaroque/wtf">Support me</a>
    ·
    <a href="https://github.com/joaroque/wtf/issues/new?labels=bug&template=bug-report---.md">Report Bug</a>
    ·
    <a href="https://github.com/joaroque/wtf/issues/new?labels=enhancement">Request Feature</a>
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->

## About The Project

[![WTF Demo][app-demo]](https://github.com/joaroque/wtf)

WTF is a terminal utility that leverages Langchain and OpenAI to read and interpret terminal errors, providing explanations that are more human-readable.

Purpose:

- Most programming languages and frameworks generate complex exception messages, making it difficult to understand the root cause.
- Existing tools typically support only English.
- Translates error outputs directly from the terminal.

<!-- GETTING STARTED -->

## Getting Started

Follow these steps to set up and run the project locally. This guide provides clear instructions to help you get started quickly.

### Prerequisites

- poetry
  ```sh
  pip install poetry
  ```
- Get a your OpenAI API Key at [https://platform.openai.com](https://platform.openai.com/settings/profile)

### Installation

_Follow the steps below to install and set up WTF locally._

1. Clone the repo
   ```sh
   git clone https://github.com/joaroque/wtf.git
   ```
2. In the project directory, install the Python packages.
   ```sh
   poetry install
   ```
3. Create and enter your API KEY in `.env`

   ```ini

   OPENAI_API_KEY = "ENTER YOUR API KEY HERE";
   ```

4. Configure the function to export terminal error output to a file. `zsh_error_log.txt`

   Add this function to the end of your `.zshrc` file.

   ```sh
   # WTF Setting
   log_errors() {
       exec 2> >(tee "$HOME/zsh_error_log.txt" >&2)
   }
   log_errors
   ```

   **ATTENTION: _WTF supports only ZSH_**

<!-- USAGE EXAMPLES -->

## Usage

[![WTF screenshot][app-screenshot]](https://github.com/joaroque/wtf)

There are two commands in WTF: `wtf` and `fuck` or `f`.

**wtf** (default): Used to explain the error in the terminal.
**fuck** or **f**: Used to correct the last command entered in the terminal.

#### Usage Instructions

1. In the project directory, activate the Poetry shell:

```sh
poetry shell
```

2. Build the WTF application:

```sh
poetry build
```

3. Verify the installation and display WTF help:

```sh
which wtf && wtf --help
```

For more information on how to use Poetry, refer to the [Poetry Documentation](https://python-poetry.org/docs/basic-usage/).

<!-- ROADMAP -->

## Roadmap

- [ ] Add support for additional shells and OS
- [ ] Refactor error extraction logic
- [ ] Add multi-language support for static texts
- [ ] Implement a CLI-based initialization system to allow users to configure `OPEN_API_KEY` during program startup

For a comprehensive list of proposed features and known issues, see the [open issues](https://github.com/joaroque/wtf/issues)

<!-- CONTRIBUTING -->

## Contributing

We welcome contributions from the community! Your involvement is vital in making WTF even better. Whether you're fixing bugs, improving documentation, adding new features, or enhancing existing ones, your help is greatly appreciated.

### How to Contribute

1. **Fork the Repository**: Create a personal copy of the repository by forking it.
2. **Create a Feature Branch**: Develop your feature or fix in a new branch.

```sh
   git checkout -b feature/YourFeatureName
```

3. **Commit Your Changes**: Clearly and concisely describe your changes in your commit messages.

```sh
    git commit -m 'Add a brief description of your feature or fix'
```

4. **Push to Your Branch**: Push your changes to your forked repository.

```sh
    git commit -m 'Add a brief description of your feature or fix'
```

5. **Open a Pull Request**: Submit your changes for review by opening a pull request in the main repository.

<!-- LICENSE -->

## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<!-- CONTACT -->

## Contact

LinkedIn - [Joaquim Roque](https://www.linkedin.com/in/joaroque/)
Project Link: [https://github.com/joaroque/wtf](https://github.com/joaroque/wtf)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[contributors-shield]: https://img.shields.io/github/contributors/joaroque/wtf.svg?style=for-the-badge
[contributors-url]: https://github.com/joaroque/wtf/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/joaroque/wtf.svg?style=for-the-badge
[forks-url]: https://github.com/joaroque/wtf/network/members
[stars-shield]: https://img.shields.io/github/stars/joaroque/wtf.svg?style=for-the-badge
[stars-url]: https://github.com/joaroque/wtf/stargazers
[issues-shield]: https://img.shields.io/github/issues/joaroque/wtf.svg?style=for-the-badge
[issues-url]: https://github.com/joaroque/wtf/issues
[license-shield]: https://img.shields.io/github/license/joaroque/wtf.svg?style=for-the-badge
[license-url]: https://github.com/joaroque/wtf/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/joaroque
[app-demo]: demo/demo.gif
[app-screenshot]: demo/demo_pic2.png
