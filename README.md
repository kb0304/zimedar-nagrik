Zimedar-Nagrik (Responsible Citizen)
=========================
⚙️ Incentivised incident reporting application

_Entry for Rajasthan Digifest Hackathon at Mohanlal Sukhadi University Udaipur_

  * [Motivation and Solution Approach](#motivation-and-solution-approach)
  * [Solution Architecture](#solution-architecture)
  * [Setup](#setup)

Motivation and Solution Approach
==================

The motivation behind chosing this problem statement is to encourage people to take part in building a better and safer India. Various incidents, be it criminal or otherwise (like Damaged Road, Accident, Garbage, Unidentified Objects, etc.) although noticed, go unreported due to lack of awareness and interest on behalf of citizens. In order to encourage people to report, an incentivised reporting app is required.

Solution Architecture
=====================
1. A user logs in to the application using his e-Mitra credentials.
2. He can report an incident by adding a description and attaching an image.
3. All the unverified incidents are visible to nearby reporters (using GPS) for verification.
3. The user can verify the incidents and report whether the incident actually happened or not.
4. On successfuly number of minimum verifications, a notification is sent to the concerned authority with the description and the details.
5. The authority on verification can decide the amount of incentive to be provided. This incentive is then broken down into two major components - the initial reporter and the verifiers.

Setup
========
1. Clone the repo ```git clone https://github.com/kb0304/zimedar-nagrik```.
2. Create a virtualenv ```pip -p python3 <virtualenv>```
3. Install the dependencies ```pip install -r requirements```
4. Make migrations and migrate ```python manage.py makemigrations``` and ```python manage.py migrate```
5. Run server ```python manage.py runserver``
