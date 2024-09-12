"""Little app to list beer.

Returns:
    _type_: _description_
"""
from flask import Flask, jsonify, request

app = Flask(__name__)


class BodyListBeer:
    """List beer."""

    def get_body(self):
        """Get list beer.

        Returns:
            List: List beer.
        """
        body = vars(BodyListBeer(self.beer, self.typeBeer, self.quantity))
        return body

    def __init__(self, b, tb, q):
        self.beer = b
        self.typeBeer = tb
        self.quantity = q


list_beer = []
list_beer.append(BodyListBeer("Paix Dieux", "triple", 2).get_body())
list_beer.append(BodyListBeer("Chimay", "triple", 1).get_body())


@app.route("/list", methods=["GET"])
def choose_beer():
    """Choose beer you want.

    Returns:
        json: ok choose beer.
    """
    beer_choose = request.args.get("beer_choose", None)
    if beer_choose:
        filtered = [m for m in list_beer if m["beer"] == beer_choose]
        if not filtered:
            return jsonify({"error": f"Don't have beer '{beer_choose}'"}), 400
        else:
            return jsonify(filtered), 200
    else:
        return jsonify(list_beer), 200


@app.route("/addBeer", methods=["POST"])
def add_beer():
    """Add beer in list of choose.

    Returns:
        json: ok add beer.
    """
    r = request.get_json()
    for m in list_beer:
        if m["beer"] == r["beer"] and m["typeBeer"] == r["typeBeer"]:
            quantity = r["quantity"] + m["quantity"]
            list_beer.remove(m)
            list_beer.append(BodyListBeer(m["beer"], m["typeBeer"], quantity).get_body())
            return (
                jsonify({"Add quantity": f"Add quantity for this beer : '{r['beer']}', new quantity : '{quantity}'"}),
                200,
            )
    list_beer.append(r)
    return jsonify({"Add beer": f"Add this beer : '{r['beer']}', quantity : '{r['quantity']}'"}), 201


@app.route("/drinkBeer", methods=["POST"])
def drink_beer():
    """Remove quantity beer is drink.

    Returns:
        json: ok or not in function of reserve of beer.
    """
    r = request.get_json()
    for m in list_beer:
        if m["beer"] == r["beer"] and m["typeBeer"] == r["typeBeer"]:
            quantity = m["quantity"] - r["quantity"]
            if quantity < 0:
                return (
                    jsonify(
                        {
                            "error": f"Don't have enough beer '{r['beer']}' in reserve, {abs(quantity)}"
                            " beer(s) missing ...",
                        },
                    ),
                    400,
                )
            elif quantity == 0:
                list_beer.remove(m)
                return (
                    jsonify(
                        {
                            "warning": f"There will be no more beer '{r['beer']}' in reserve after this one !!!",
                        },
                    ),
                    200,
                )
            list_beer.append(BodyListBeer(m["beer"], m["typeBeer"], quantity).get_body())
            return (
                jsonify(
                    {
                        "Beer drink": f"New quantiy for beer '{r['beer']}' in reserve : {abs(quantity)}",
                    },
                ),
                200,
            )
    return jsonify({"error": f"Don't have beer '{r['beer']}' in the reserve ...."}), 404


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)
