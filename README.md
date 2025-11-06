# Online-Count


<h1>Overview</h1>
The online_count() function counts how many users are currently marked as "online" within a given dictionary of user statuses.<br>
It loops through each user and increments the count for every user whose status equals "online".<br>

<h2>How it works</h2>
<ul>
<li>The function accepts a dictionary of user names and their corresponding status values (e.g., "online" or "offline").</li>
<li>It creates a variable count to track the number of users online.</li>
<li>It loops through each key (name) in the dictionary:</li>
  <ul>
    <li>If the value for that key is "online", it increments count by 1.</li>
  </ul>
<li>After looping through all users, the function returns the total count.</li>
</ul>


<h3>Example</h3>
statuses = {
    "Bryan": "online",
    "Marcela": "offline",
    "Alex": "online",
    "Jordan": "offline"
}

result = online_count(statuses)

print(result)


<h3>Output</h3>
2

