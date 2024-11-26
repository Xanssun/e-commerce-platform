DC = docker compose
EXEC = docker exec -it
LOGS = docker logs
ENV = --env-file .env
ORDER_APP_FILE = ../../docker_compose/order-app.yaml
ORDER_APP_CONTAINER = order-app

.PHONY: order-app
order-app:
	${DC} -f ${ORDER_APP_FILE} ${ENV} up --build -d

.PHONY: order-app-down
order-app-down:
	${DC} -f ${ORDER_APP_FILE} down

.PHONY: order-app-shell
order-app-shell:
	${EXEC} ${ORDER_APP_CONTAINER} bash

.PHONY: order-app-logs
order-app-logs:
	${LOGS} ${ORDER_APP_CONTAINER} -f


.PHONY: order-all
order-all:
	${DC} -f ${ORDER_APP_FILE} ${ENV} up --build -d
