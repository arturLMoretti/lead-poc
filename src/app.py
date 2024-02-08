import os
import uuid
import boto3
from flask import Flask, redirect, render_template, request

from dynamo import Dynamo
from lead import Lead

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/leads")
def leads():
    return render_template("leads.html")


@app.route("/leads/create", methods=["POST", "GET"])
def create_lead():
    region_name = os.environ.get("AWS_REGION")
    aws_access_key_id = os.environ.get("AWS_ACCESS_KEY_ID")
    aws_secret_access_key = os.environ.get("AWS_SECRET_ACCESS_KEY")
    connection = boto3.resource(
        "dynamodb",
        region_name=region_name,
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key,
    )
    if request.method == "POST":
        try:
            dynamo = Dynamo(table_name="poc-leads", connection=connection)
            lead = Lead(**request.form)
            dynamo.save(lead=lead)
            return "Lead criado com sucesso"
        except Exception as e:
            print(e)
            return "Erro ao criar lead"
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
