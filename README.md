>[!WARNING]
>CURRENTLY UNDER DEVELOPMENT


# Natural Language Processing with Python

Get the grammar, parts of speech, and split into words from a different input sentence everytime from the CLI

some grammar:
- NNP -> proper noun
- VBZ -> verb 3rd person singular present
- PRP -> pronoun
- RBR -> adverb comparative

---

## How it works

```
git clone https://github.com/gutiluis/nat-lang-proc.git
```

### build image
```
docker-compose build
```

### run interactively the input inside the unix terminal
```
docker-compose run -rm nlp-app
```

### bash it with python

```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
chmod +x nlp.py
python3 nlp.py
```

---

## Tech-Stack

- Python
- Docker

---

## Contributing

If you are interested in reporting/fixing issues and contributing directly to the code base, please see [CONTRIBUTING.md](https://github.com/gutiluis/.github/blob/main/CONTRIBUTING.md) for more information on what we're looking for and how to get started.

---

## Code of Conduct

By participating in this project, you agree to abide by our [Code of Conduct](https://github.com/gutiluis/.github/blob/main/CODE_OF_CONDUCT.md).

---

## Security Policy

If you discover a security vulnerability, please review our [Security Policy](https://github.com/gutiluis/.github/blob/main/SECURITY.md) for reporting guidelines.

---

## Support

If you run into any issues or have questions, please check our [SUPPORT.md](https://github.com/gutiluis/.github/blob/main/SUPPORT.md) file for guidance, or reach out through one of our community channels below.

---

## Community

Info on reporting bugs, getting help, finding third-party tools and sample apps, and more can be found on our **Community** channels:
* **Discord:** [Community channel](https://discord.gg/5xdAFuadP)
* **Slack Workspace:** [technobool.slack.com](https://technobool.slack.com)
* **GitHub Discussions:** [Open a discussion](https://github.com/gutiluis/nat-lang-proc/discussions)

---

## License

[MIT LICENSE](LICENSE)
