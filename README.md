# cfb-picker-backend
Django Backend for attempting to pick the entire SEC football schedule before the season

![Unit Tests](https://github.com/andmehta/cfb-picker-backend/workflows/django.yml/badge.svg)

## How to Run
1. [Clone this repo](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository)
2. Add your own database password file `db/password.txt` and type in some password. The contents don't *actually* matter, the point is that the password is never part of the VCS
3. [Install docker and docker compose](https://www.docker.com/products/docker-desktop/?) if you haven't already
4. use docker compose to boot up the installation on your local machine
```shell
docker compose up 
```
5. access the site at https://localhost:8000/

## Set up a Development environment
1. Do steps 1-3 for How to Run
2. Then use Pycharm and the run configuration "runserver" so you can use things like the debugger
3. This will instantiate a different postgres DB/network, so don't worry about issues with the test environment 


### TODO
- [x] Sign-in
- [x] clean up of UI (use bootstrap and base html)
- [x] CI/CD unit tests
- [ ] Auto-deployment
- [ ] Game Results saved and shown in Games Screen
- [ ] API and JWT token
- [ ] Integrate against [cfbpicker](https://github.com/andmehta/cfbpicker) react app