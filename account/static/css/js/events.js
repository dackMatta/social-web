    // Assuming you have the js-cookie library loaded on your page
    const csrftoken = Cookies.get('csrftoken');
    document.addEventListener('DOMContentLoaded', (event) => {
        // DOM Loaded
// In your script.js file
document.addEventListener('DOMContentLoaded', (event) => {
    // Your code here
    const csrftoken = Cookies.get('csrftoken');
    //...
});
        {% endblock %}
    });