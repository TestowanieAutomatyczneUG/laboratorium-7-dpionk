import math
import unittest

class Program:
    def statement(self, invoice, plays):
        total_amount = 0
        volume_credits = 0
        result = f'Statement for {invoice["customer"]}\n'

        def format_as_dollars(amount):
            return f"${amount:0,.2f}"

        for perf in invoice['performances']:
            play = plays[perf['playID']]
            if play['type'] == "tragedy":
                this_amount = 40000
                if perf['audience'] > 30:
                    this_amount += 1000 * (perf['audience'] - 30)
            elif play['type'] == "comedy":
                this_amount = 30000
                if perf['audience'] > 20:
                    this_amount += 10000 + 500 * (perf['audience'] - 20)

                this_amount += 300 * perf['audience']

            else:
                raise ValueError(f'unknown type: {play["type"]}')

            # add volume credits
            volume_credits += max(perf['audience'] - 30, 0)
            # add extra credit for every ten comedy attendees
            if "comedy" == play["type"]:
                volume_credits += math.floor(perf['audience'] / 5)
            # print line for this order
            result += f' {play["name"]}: {format_as_dollars(this_amount/100)} ({perf["audience"]} seats)\n'
            total_amount += this_amount

        result += f'Amount owed is {format_as_dollars(total_amount/100)}\n'
        result += f'You earned {volume_credits} credits\n'
        return result

class Test_Program(unittest.TestCase):

    def setUp(self):
        self.temp = Program()

    def testInstance(self):
        self.assertIsInstance(self.temp, Program)

    def test_correct(self):
        self.assertEqual( "Statement for BigCo\n Hamlet: $650.00 (55 seats)\n As You Like It: $580.00 (35 seats)\n Othello: $500.00 (40 seats)\nAmount owed is $1,730.00\nYou earned 47 credits\n", self.temp.statement({
  "customer": "BigCo",
  "performances": [
    {
      "playID": "hamlet",
      "audience": 55
    },
    {
      "playID": "as-like",
      "audience": 35
    },
    {
      "playID": "othello",
      "audience": 40
    }
  ]
},
    {
        "hamlet": {"name": "Hamlet", "type": "tragedy"},
        "as-like": {"name": "As You Like It", "type": "comedy"},
        "othello": {"name": "Othello", "type": "tragedy"}
    }
))

    def test_correct_2(self):
        self.assertEqual("Statement for Some Company\n Hamlet: $550.00 (45 seats)\n Idk: $1,100.00 (100 seats)\n Some play: $5,100.00 (500 seats)\nAmount owed is $6,750.00\nYou earned 575 credits\n", self.temp.statement({
  "customer": "Some Company",
  "performances": [
    {
      "playID": "hamlet",
      "audience": 45
    },
    {
      "playID": "idk",
      "audience": 100
    },
    {
      "playID": "some play",
      "audience": 500
    }
  ]
},
{
  "hamlet": {"name": "Hamlet", "type": "tragedy"},
  "idk": {"name": "Idk", "type": "comedy"},
  "some play": {"name": "Some play", "type": "tragedy"}
}))

    def test_correct_3(self):
        self.assertEqual("Statement for Some Company\n Hamlet: $400.00 (20 seats)\n Idk: $330.00 (10 seats)\n Some play: $1,300.00 (120 seats)\nAmount owed is $2,030.00\nYou earned 92 credits\n",
                         self.temp.statement({
  "customer": "Some Company",
  "performances": [
    {
      "playID": "hamlet",
      "audience": 20
    },
    {
      "playID": "idk",
      "audience": 10
    },
    {
      "playID": "some play",
      "audience": 120
    }
  ]
},
{
  "hamlet": {"name": "Hamlet", "type": "tragedy"},
  "idk": {"name": "Idk", "type": "comedy"},
  "some play": {"name": "Some play", "type": "tragedy"}
}))

    def test_correct_4(self):
        self.assertEqual("Statement for Some Company\n Hamlet: $400.00 (20 seats)\nAmount owed is $400.00\nYou earned 0 credits\n", self.temp.statement({
  "customer": "Some Company",
  "performances": [
    {
      "playID": "hamlet",
      "audience": 20
    }
  ]
},
{
  "hamlet": {"name": "Hamlet", "type": "tragedy"},
}))

    def test_correct_5(self):
        self.assertEqual("Statement for Some Company\n Hamlet: $500.00 (40 seats)\nAmount owed is $500.00\nYou earned 10 credits\n", self.temp.statement(
            {
                "customer": "Some Company",
                "performances": [
                    {
                        "playID": "hamlet",
                        "audience": 40
                    }
                ]
            },
            {
                "hamlet": {"name": "Hamlet", "type": "tragedy"},
            }
        ))

    def test_correct_6(self):
        self.assertEqual("Statement for Some Company\n Hamlet: $620.00 (40 seats)\nAmount owed is $620.00\nYou earned 18 credits\n", self.temp.statement(
            {
                "customer": "Some Company",
                "performances": [
                    {
                        "playID": "hamlet",
                        "audience": 40
                    }
                ]
            },
            {
                "hamlet": {"name": "Hamlet", "type": "comedy"},
            }
        ))
    def test_wrong_play_type(self):
        self.assertRaises(ValueError, self.temp.statement,{
  "customer": "BigCo",
  "performances": [
    {
      "playID": "hamlet",
      "audience": 55
    },
    {
      "playID": "as-like",
      "audience": 35
    },
    {
      "playID": "othello",
      "audience": 40
    }
  ]
},
    {
        "hamlet": {"name": "Hamlet", "type": "gdfggdfgfdg"},
        "as-like": {"name": "As You Like It", "type": "comedy"},
        "othello": {"name": "Othello", "type": "tragedy"}
    }
)

    def test_wrong_play_type_2(self):
        self.assertRaises(ValueError, self.temp.statement, {
                "customer": "BigCo",
                "performances": [
                    {
                        "playID": "hamlet",
                        "audience": 55
                    },
                    {
                        "playID": "as-like",
                        "audience": 35
                    },
                    {
                        "playID": "othello",
                        "audience": 40
                    }
                ]
            },
                    {
                        "hamlet": {"name": "Hamlet", "type": "comedy"},
                        "as-like": {"name": "As You Like It", "type": []},
                        "othello": {"name": "Othello", "type": "tragedy"}
                    }
            )

    def test_wrong_play_type_3(self):
        self.assertRaises(ValueError, self.temp.statement, {
                "customer": "BigCo",
                "performances": [
                    {
                        "playID": "hamlet",
                        "audience": 55
                    },
                    {
                        "playID": "as-like",
                        "audience": 35
                    },
                    {
                        "playID": "othello",
                        "audience": 40
                    }
                ]
            },
                    {
                        "hamlet": {"name": "Hamlet", "type": "comedy"},
                        "as-like": {"name": "As You Like It", "type": "comedy"},
                        "othello": {"name": "Othello", "type": None}
                    }
            )
    def tearDown(self):
        self.temp = None
