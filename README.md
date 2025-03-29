# Activity Planner by Weather
#### Description:

As a parent on parental leave, I often find myself pondering a daily question: what should I do with my toddler daughter? This project, developed as a practical tool for my everyday life, leverages real-time weather data to provide tailored activity and clothing suggestions. It’s a perfect blend of utility and creativity, designed to simplify decision-making for parents like me.

The program is built using Python and uses several key programming skills I learned from the CS50 course: API integration, data storing and reading with dictionaries, and conditional logic. At its core, it utilizes the OpenWeather API, a free service offering real-time weather data with a generous limit of 1,000 API calls per day. By sending a request with a user-specified city name, the program retrieves essential weather details—country, city, weather condition, and temperature in Celsius—and stores them in a dictionary for easy access.

The functionality extends beyond data retrieval. I’ve crafted custom output result to enhance the user experience. One maps weather conditions (e.g., "Clear," "Rain," "Snow") to child-friendly activity suggestions, such as "Go for a walk in nature" for clear or cloudy days, or "Stay indoors and read a book together" during thunderstorms. Another dictionary pairs weather types with emoji icons (e.g.,  for "Clear,"  for "Rain"), making the output visually engaging. Additionally, a temperature-based clothing recommendation system uses conditional statements to suggest appropriate outdoor clothings, like 

```

Today in Uppsala County, SE: ☁️ Clouds, 5.69°C. 

Suggested activity: Go for a walk in the nature
Suggested clothing: Wear a warm jacket and thick pants

```

To use the program, simply input a city name—like "Uppsala," where I live in Sweden—and it delivers a concise, actionable report. For example: "Today in Uppsala County, SE:  Clouds, 8.69°C. Suggested activity: Go for a walk in nature. Suggested clothing: Wear a warm jacket and thick pants." If the API call fails (due to an invalid city or key issue), the program exits with an error message.

This tool not only streamlines my daily planning but also demonstrates practical applications of coding in real life. It’s a small yet powerful assistant for any parent navigating unpredictable weather with a toddler!

