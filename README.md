<a name="readme-top"></a>
  <h1 align="center">range_slicer by citb0in</h1>
<div align="center">
  <p align="center">
    <br />
    <a href="https://github.com/citb0in/range_slicer/issues">Report Bug</a>
    ·
    <a href="https://github.com/citb0in/range_slicer/issues">Request Feature</a>
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
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
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

This small tool was created as a result of [this discussion on bitcointalk.org](https://bitcointalk.org/index.php?topic=5421165.0).


<p align="right">(<a href="#readme-top">back to top</a>)</p>


### Built With

Python3 on GNU/Linux

[![Python3][Python3.com]][Python3-url]


<p align="right">(<a href="#readme-top">back to top</a>)</p>


## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

Note: Python2 is not supported.

* Python3 libs
```sys, pprint, argparse```

### Installation

1. Ensure you are running Python3
   ```sh
   python3 -V
   ```

2. Clone this repository
   ```sh
   git clone https://github.com/citb0in/range_slicer.git
   ```
   
3. Either make the python program executable
   ```sh
   chmod +x ./range_slicer.py
   ```
   and run it by
   ```sh
   ./range_slicer.py
   ```
   
   or just execute it by
   ```sh
   python3 range_slicer.py
   ```
<p align="right">(<a href="#readme-top">back to top</a>)</p>


## Usage

Current version allows two ways of execution. The range is mandatory and must always be entered as a parameter so that the program has something to do. By default, the program will use the "n slices" mode, where n is the number of slices desired. If no input is made for 'n', the default value 2 is used.

However, there are also cases where the user wants a certain size of the slices to be generated and doesn't care about the total number of slices to be generated. I integrated this "chunks" mode that can be used with the command line switch -c (for chunks).

Examples:

Range 20 - 90 will be sliced into 15 equal parts
  ```sh
  ./range_slicer.py -r 20 90 -n 15
  ```
  
Range 20 - 90 will be sliced into 15 equal parts with non-overlapping range edges
  ```sh
  ./range_slicer.py -r 20 90 -n 15 -nov
  ```

Range 20 - 95 will be sliced into chunks with size of 10 
  ```sh
  ./range_slicer.py -r 20 95 -c -n 10
  ```

Display version
  ```sh
  ./range_slicer.py -V
  ```
<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ROADMAP -->
## Roadmap

- [x] Add Changelog
- [x] Add back to top links
- [ ] Implement input validation
- [ ] Add "non-overlapping range edges" function to n-slices mode
- [ ] Add hex support
- [ ] Multi-language Support
    - [ ] Spanish
    - [ ] French
    - [ ] Chinese

See the [open issues](https://github.com/citb0in/range_slicer/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the GPLv3 License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

[@citb0in](https://bitcointalk.org)

Project Link: [https://github.com/citb0in/range_slicer](https://github.com/citb0in/range_slicer)


<p align="right">(<a href="#readme-top">back to top</a>)</p>


## Acknowledgments

Helpful ressources and credits to:

* [Choose an Open Source License](https://choosealicense.com)
* [GitHub Emoji Cheat Sheet](https://www.webpagefx.com/tools/emoji-cheat-sheet)
* [Img Shields](https://shields.io)
* [GitHub Pages](https://pages.github.com)
* [Best Best-README-Template](https://github.com/othneildrew/Best-README-Template)
* [Font Awesome](https://fontawesome.com)


<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/citb0in/range_slicer.svg?style=for-the-badge
[contributors-url]: https://github.com/citb0in/range_slicer/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/citb0in/range_slicer.svg?style=for-the-badge
[forks-url]: https://github.com/citb0in/range_slicer/network/members
[stars-shield]: https://img.shields.io/github/stars/citb0in/range_slicer.svg?style=for-the-badge
[stars-url]: https://github.com/citb0in/range_slicer/stargazers
[issues-shield]: https://img.shields.io/github/issues/citb0in/range_slicer.svg?style=for-the-badge
[issues-url]: https://github.com/citb0in/range_slicer/issues
[license-shield]: https://img.shields.io/github/license/citb0in/range_slicer.svg?style=for-the-badge
[license-url]: https://github.com/citb0in/range_slicer/blob/master/LICENSE.txt
[Python3.com]: https://www.python.org/static/img/python-logo@2x.png
[Python3-url]: https://www.python.org/download/releases/3.0
