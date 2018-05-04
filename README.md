<div align="center">

# Interview Test 4
</div>

## Development Environment

Note: [Docker][docker-link] and [Docker Compose][docker-compose-link] must be installed in your
environment (they come bundled for Mac).

```bash
# Clone repo
mkdir test_app && cd $_ && git clone https://github.com/jourdanrodrigues-tests/test_4/ .
# Run the servers (might take a while)
docker-compose up
```

After running the second command, you should have access to the frontend app at
[https://localhost:3000/][localhost-3000] and the backend app at
[https://localhost:5000/][localhost-5000]

## Production Environment

*Coming soon!*

## Test Requirements

Check the original test requirements [here](REQUIREMENTS.md). Also, check the [UI reference](reference.png).

[localhost-3000]: https://localhost:3000/
[localhost-5000]: https://localhost:5000/
[docker-link]: https://www.docker.com/community-edition#download
[docker-compose-link]: https://docs.docker.com/compose/install/
