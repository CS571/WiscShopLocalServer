# Course Guide API

The following API can be accessed at `https://cs571.cs.wisc.edu/api/react`

| Route                                   | Auth Required | Token Required | Get | Post | Put | Delete |
|-----------------------------------------|---------------|----------------|-----|------|-----|--------|
| /classes                                |               |                |  ✔︎  |      |     |        |
| /students/5022025924/classes/completed/ |               |                |  ✔︎  |      |     |        |

## Get all courses

Returns a list of all courses in the following format:

```json
[
    {
        "credits": <number of credits for the course>,
        "description": <course description>,
        "keywords": <1D list of string keywords>,
        "name": <course name>,
        "number": <unique course number>,
        "requisites": <2D list of course requisites>,
        "sections": [
            {
                "instructor": <instructor name>,
                "location": <section location>,
                "subsections": [
                    {
                        "location": <subsection location>,
                        "time": {
                            <weekday>: <time range>, ...
                        },
    					"number": <subsection number>
                    }
                ],
                "time": {
                <weekday>: <time range>, ...
                },
				"number": <section number>
            }, ...
        ],
        "subject": <course subject>
    }, ...
]
```

- The list of course requisites consists of 1D lists with AND operations between them. Each 1D list has OR operations between elements. For example: `[[A, B], [C, D, E], [F]]` means that the requisites are `(A OR B) AND (C OR D OR E) AND (F)`. The requisites will be represented as the course's alpha-numeric key used in the outermost object.
- Sections and subsections can have any number of times. Each time's key is a weekday in all lowercase ("monday", "tuesday", "wednesday", ...). Each time's value is a string with the following format: `"<12 hour time><am or pm> - <12 hour time><am or pm>"`. An example of this would be `"11:45am - 12:35pm"`.
- Each course has exactly one subject

**URL** : `/api/react/classes`

**Method** : `GET`

**Auth required** : NO

### Success Response

**Code** : `200 OK`

**Content example**
```json
[
    {
        "credits": 3, 
        "description": "Introduces software development of user interfaces (UIs). Build competence in implementing UIs using state-of-the-art (1) UI paradigms, such as event-driven interfaces, direct-manipulation interfaces, and dialogue-based interaction; (2) methods for capturing, interpreting, and responding to different forms of user input and states, including pointing, text entry, speech, touch, gestures, user activity, context, and physiological states; and (3) platform-specific UI development APIs, frameworks, and toolkits for multiple platforms including web/mobile/desktop interfaces, natural user interfaces, and voice user interfaces. Learn about the fundamental concepts, technologies, algorithms, and methods in building user interfaces, implement UIs using of state-of-the-art UI development tools, and build a UI development portfolio.", 
        "keywords": [
          "computer", 
          "science", 
          "building", 
          "user", 
          "interface", 
          "interfaces", 
          "design", 
          "ui"
        ], 
        "name": "Building User Interfaces", 
        "number": "COMP SCI 571", 
        "requisites": [
          [
            "COMP SCI 400"
          ]
        ], 
        "sections": [
          {
            "instructor": "Yuhang Zhao", 
            "location": "180 Science Hall", 
            "number": "LEC_001", 
            "subsections": [], 
            "time": {
              "thursday": "11:00am - 12:15pm", 
              "tuesday": "11:00am - 12:15pm"
            }
          }
        ], 
        "subject": "Computer Science"
    }
]
```

## Get completed courses of a student

Returns a list completed courses of a student

**URL** : `/api/react/students/5022025924/classes/completed/`

**Method** : `GET`

**Auth required** : NO

### Success Response

**Code** : `200 OK`

**Content example**

```json
{
  "data": [
    "PSYCH 202", 
    "COMP SCI 200", 
    "COMP SCI 300", 
    "CHEM 103", 
    "MATH 114", 
    "MATH 221"
  ]
}
```