MKDIR=sudo mkdir -p
RM=sudo rm -rf
OWN=sudo chown -R

all: up

set_up:
	$(MKDIR) /home/mozennou/data/inventory
	$(MKDIR) /home/mozennou/data/billing
	$(OWN) 70:70 /home/mozennou/data

up: set_up
	docker compose -f ./srcs/compose.yml up

up_build: set_up
	docker compose -f ./srcs/compose.yml up --build

fclean:
	docker compose -f ./srcs/compose.yml down
 