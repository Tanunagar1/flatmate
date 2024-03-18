from flask.views import MethodView
from flask import Flask, render_template, request
from wtforms import Form, StringField, IntegerField, SubmitField
from files import flat
import pdfkit

app = Flask(__name__)


class Homepage(MethodView):
    def get(self):
        return render_template("index.html")


class BillForm(Form):
    amount = IntegerField("Bill Amount: ")
    period = StringField("Bill Period: ")
    name1 = StringField("Name")
    days_in_house1 = IntegerField("Days in the house")
    name2 = StringField("Name")
    days_in_house2 = IntegerField("Days in the house")
    button = SubmitField("Calculate")


class BillFormPage(MethodView):
    def get(self):
        billform = BillForm()

        return render_template("bill_form_page.html", billform=billform, result=None)


class ResultPage(MethodView):
    def post(self):
        bill_form = BillForm(request.form)
        if bill_form.validate():

            the_bill = flat.Bill(bill_form.amount.data, bill_form.period.data)
            flatmate1 = flat.Flatmates(bill_form.name1.data, bill_form.days_in_house1.data)
            flatmate2 = flat.Flatmates(bill_form.name2.data, bill_form.days_in_house2.data)
            amount1 = round(flatmate1.pays(the_bill, flatmate2), 2)
            amount2 = round(flatmate2.pays(the_bill, flatmate1), 2)
            total = float(bill_form.amount.data)
            return render_template("resultpage.html",billform=bill_form ,total=total,
                                   period=bill_form.period.data, name1=flatmate1.name, amount1=amount1,
                                   name2=flatmate2.name, amount2=amount2)

        else:
            message = "Form validation failed"
            return render_template("bill_form_page.html", billform=bill_form, total=None, message=message)


app.add_url_rule("/", view_func=Homepage.as_view("home_page"))
app.add_url_rule("/bill_form_page", view_func=BillFormPage.as_view("bill_form_page"))
app.add_url_rule("/resul_page", view_func=ResultPage.as_view("result_page"))

if __name__ == "__main__":
    app.run(debug=True)
