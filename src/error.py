from flask import Blueprint, render_template, Response
from werkzeug.exceptions import NotFound, InternalServerError, Forbidden

error = Blueprint("error", __name__, template_folder="template", static_folder="static")


@error.app_errorhandler(404)
def error_404(error: NotFound) -> str:
    return render_template("error/error.html", error=error, code=404)


@error.app_errorhandler(500)
def error_500(error: InternalServerError) -> Response:
    return render_template("error/error.html", error=error, code=500)


@error.app_errorhandler(403)
def error_403(error: Forbidden) -> Response:
    return render_template("error/error.html", error=error, code=403)
