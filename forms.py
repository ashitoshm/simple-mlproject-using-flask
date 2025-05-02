import pandas as pd
from flask_wtf import FlaskForm
from wtforms import (
    SelectField,
    DateField,
    TimeField,
    IntergerField,
    SubmitField
)
from wtforms.validators import DataRequired

train = pd.read_csv("data/train.csv")
val = pd.read_csv("data/val.csv")
X_data = pd.concat([train, val], axis=0).drop(columns="price")

class InputForm(FlaskForm):
    airline = SelectField(
        label="Airline",
        choices=X_data.airline.unique().to_list(),
        validators=[DataRequired()]
    )

    date_of_journey = DateField(
        label="Date of Journey",
        validators=[DataRequired()]
    )

    source = SelectField(
        label="Source",
        choices=X_data.source.unique().to_list(),
        validators=[DataRequired()]
    )
    destination = SelectField(
        label="Destinantion",
        choices=X_data.destinantion.unique().to_list(),
        validators=[DataRequired()]
    )
    dep_time = TimeField(
        label="Departure Time"
        validators=[DataRequired()]
    )
    arrival_time = TimeField(
        label="Arrival Time"
        validators=[DataRequired()]
    )
    duration = IntergerField(
        label ="Duration",
        validators=[DataRequired()]
    )
    total_stops = IntergerField(
        label ="Total Stops",
        validators=[DataRequired()]
    )
    additional_info = SelectField(
        label="Additional Info",
        choices = X_data.additional_info.unique().tolist(),
        validators=[DataRequired()]
    )
    submit = SubmitField("Predict")


