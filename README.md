# cfb-picker-backend
Django Backend for attempting to pick the entire SEC football schedule before the season

![Unit Tests](https://github.com/andmehta/cfb-picker-backend/actions/workflows/django.yml/badge.svg)

## How to Run
1. [Clone this repo](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository)
2. Add your own database password file `db/prod-db-password.txt` and type in some password. The contents don't *actually* matter, the point is that the password is never part of the VCS
3. Add a file `db/django-secret-key.txt`. Recommend [creating one here](https://djecrety.ir)
4. Finally, add a directory and a file `.envs/fake-production.env` and fill with values needed
5. [Install docker and docker compose](https://www.docker.com/products/docker-desktop/?) if you haven't already
6. Use docker compose to boot up the installation on your local machine
```shell
docker compose up 
```
7. Access the site at https://localhost:8000/

## Set up a Development environment
1. Do steps 1-5 for [How to Run](#how-to-run)
2. Then use Pycharm and the run configuration "runserver" so you can use things like the debugger
3. This will instantiate a different postgres DB/network, so don't worry about issues with the test environment 


### TODO
- [x] Sign-in
- [x] clean up of UI (use bootstrap and base html)
- [x] CI/CD unit tests
- [ ] ~~Auto-deployment~~  no auto after some reading. But setting up terraform and GCP
- [ ] Game Results saved and shown in Games Screen
- [ ] API and JWT token
- [ ] investigate [fly.io](https://fly.io/docs/django/getting-started/existing/) for hosting cost savings
- [ ] Integrate against [cfbpicker](https://github.com/andmehta/cfbpicker) react app