from src import *

# This is an example code for use case of the form builder. It is not meant to be used in production.
# You can copy this to reft and run main.py

title = "Section A"
tags = None

fields = [
    Text(name = "name", label = "Name"),
    FieldGroup(
        fields = [
            Number(name = "age", label = "Age"),
            DropDown(name = "sex", label = "Sex", options = ["Male", "Female"]),
            DropDown(name = "cs", label = "CS", options = ["Single", "Married", "Divorced", "Widowed"]),
            Number(name = "hrn", label = "HRN")
        ],
        columns = 4
    ),
    Text(name = "address", label = "Address"),
    FieldGroup(
        fields = [
            Date(name = "admission-date", label = ""),
            Time(name = "admission-time", label = ""),
            TextArea(name = "complaint", label = "Chief Complaint"),
            TextArea(name = "history", label = "History of Present Illness")
        ],
        columns = 2
    ),
    Text(name = "admitting-impression", label = "Admitting Impression"),
    FieldGroup(
        fields = [
            DropDown(name = "blood-type", label = "Blood type/RH", options = [
                "A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"
            ]),
            DropDown(name = "hbsag", label = "HBsAg", options = ["Positive", "Negative", "Pending"])
        ],
        columns = 2
    ),
    FieldGroup(
        fields = populate(Number, ("name", "label", "min"), (
            ("gravida", "Gravida", 0),
            ("para", "Para", 0),
            ("full-term", "Full Term", 0),
            ("pre-term", "Pre Term", 0),
            ("abortions", "Abortions", 0),
            ("living-children", "Living Children", 0)
        )),
        columns = 4
    ),
    FieldGrid(
        columns = [
            Number(name = "preg-order", label = "Pregnancy Order", min = 0),
            DropDown(name = "outcome", label = "Outcome/Delivery", options = ["NSVD", "CS", "Abortion"]),
            Number(name = "year", label = "Year", min = 0),
            Number(name = "gestation-period", label = "Gestation completed (weeks)", min = 0),
            DropDown(name = "sex", label = "Sex", options = ["Male", "Female"]),
            Number(name = "birth-weight", label = "Birth Weight", min = 0),
            DropDown(name = "status", label = "Present Status", options = ["Alive", "Deceased"]),
            Text(name = "complications", label = "Complications/Abnormalities")
        ]
    ),
    Radio(name = "family-size", label = "Desired Family Size", options = ["1", "2", "3", "4"],
        non_opt = Option(label = "more{{size|Specify}}", value = "more")
    ),
    CheckboxList(name = "contraceptive-history", label = "Contraceptive History", options = ["None", "Pills", "IUD", "Rhythm", "Condom", "Others"]),
    CheckboxList(name = "educ-profile", label = "Educational Profile", options = ["None", "Primary", "Secondary"],
        non_opt = Option(label = "College{{university|University}}")
    ),
    FieldGroup(
        fields = [
            Radio(name = "socio-economic-profile", label = "Socio-economic Profile", options = [
                Option(label = "Dependent/Unemployed", value = "dependent"),
                Option(label = "Employed/Self/Others", value = "employed"),
                Option(label = "Casual Worker", value = "casual")
            ]),
            Radio(name = "income", label = "Income", options = [
                Option(label = "Below minimum wage", value = "below-min"),
                Option(label = "Minimum", value = "min"),
                Option(label = "Above minimum", value = "above-min")
            ])
        ], 
        columns = 2
    ),
    FieldGroup(
        name = "present-pregnancy",
        title = "Present Pregnancy",
        fields = [
            *populate(Date, ("name", "label"), (
                ("last-menstrual-period", "Last Menstrual Period"),
                ("previous-menstrual-period", "Previous Menstrual Period"),
                ("date-of-confinement", "Date of Confinement")    
            )),
            Number(name = "age-of-gestation", label = "Age of Gestation (weeks)", min = 0)
        ],
        columns = 2
    ),
    FieldGroup(
        name = "menstrual-cycle",
        label = "Menstrual Cycle",
        fields = populate(
            Number, ("name", "label", "min"), (
                ("menarche", "Menarche", 0),
                ("interval", "Interval", 0),
                ("duration", "Duration", 0)
            )
        ),
        columns = 4
    )
]