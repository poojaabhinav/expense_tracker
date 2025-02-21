// Dark Mode Toggle
const toggle = document.getElementById("dark-mode-toggle");
toggle.addEventListener("click", () => {
    document.body.classList.toggle("dark-mode");
    localStorage.setItem("darkMode", document.body.classList.contains("dark-mode"));
});

// Load Dark Mode Preference
if (localStorage.getItem("darkMode") === "true") {
    document.body.classList.add("dark-mode");
}

// Chart Data (Fetched from Flask)
const chartData = JSON.parse('{{ chart_data | tojson | safe }}');
const labels = chartData.map(item => item.category);
const values = chartData.map(item => item.total_amount);

// Render Chart
const ctx = document.getElementById("expenseChart").getContext("2d");
new Chart(ctx, {
    type: "doughnut",
    data: {
        labels: labels,
        datasets: [{
            data: values,
            backgroundColor: ["#ff6384", "#36a2eb", "#ffce56", "#4bc0c0", "#9966ff"],
        }]
    }
});
