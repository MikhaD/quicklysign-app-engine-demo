from flask import Blueprint, request
from setup import datastore_client

api = Blueprint("api", __name__, url_prefix="/api")

@api.route("skills", methods=["GET"])
def skills():
	query = datastore_client.query(kind="skill")
	query.order = ["-years"]

	skills = query.fetch(limit=int(request.args.get("count", 10)))
	return [skill for skill in skills]


@api.route("projects", methods=["GET"])
def projects():
	query = datastore_client.query(kind="project")

	projects = query.fetch(limit=int(request.args.get("count", 3)))
	return [project for project in projects]


@api.route("jobs", methods=["GET"])
def jobs():
	query = datastore_client.query(kind="job")

	jobs = query.fetch(limit=int(request.args.get("count", 3)))
	return [job for job in jobs]