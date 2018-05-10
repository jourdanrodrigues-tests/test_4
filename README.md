<div align="center">

# Interview Test 4
</div>

## Environment setup

Notes:

- The script [`compose.sh`](compose.sh) is a wrapper for the `docker-compose` command - see
[Docker Compose docs][docker-compose-docs-link].

- [Docker][docker-link] and [Docker Compose][docker-compose-link] must be installed in your
environment (they come bundled for Mac).

```bash
# Clone repo
mkdir yousician-test && cd $_ && git clone https://github.com/jourdanrodrigues-tests/test_4/ .
```

### Development

```bash
./compose.sh up
```

### Production

```bash
./compose.sh prod up
```

After running the `up` command, you should have access to the frontend app at
[http://localhost:3000/][localhost-3000] and the backend app at
[http://localhost:5000/][localhost-5000]

## Test Requirements

Check the original test requirements [here](REQUIREMENTS.md). Also, check the [UI reference](reference.png).

[localhost-3000]: http://localhost:3000/
[localhost-5000]: http://localhost:5000/
[docker-link]: https://www.docker.com/community-edition#download
[docker-compose-link]: https://docs.docker.com/compose/install/
[docker-compose-docs-link]: https://docs.docker.com/compose/reference/
