// ======================================================
// DOM ELEMENTS
// ======================================================

const queryInput = document.getElementById("query");
const researchButton = document.getElementById("research-btn");
const reportOutput = document.getElementById("report-output");

// Agent Status Elements
const agentElements = {
    "Planner": document.getElementById("planner"),
    "Search Agent": document.getElementById("search"),
    "Research Agent": document.getElementById("research"),
    "Writer": document.getElementById("writer")
};

// ======================================================
// CONFIGURATION
// ======================================================

const API_URL = "http://127.0.0.1:8000";

// ======================================================
// UI FUNCTIONS
// ======================================================

function showPlaceholder(title, message = "") {

    reportOutput.innerHTML = `
        <div class="placeholder">
            <h3>${title}</h3>
            <p>${message}</p>
        </div>
    `;

}

function displayReport(report) {

    reportOutput.innerHTML = `
        <pre>${report}</pre>
    `;

}

// ======================================================
// AGENT FUNCTIONS
// ======================================================

function resetAgents() {

    Object.values(agentElements).forEach(agent => {

        const indicator = agent.querySelector(".status");

        indicator.classList.remove(
            "running",
            "completed"
        );

        indicator.classList.add("waiting");

    });

}

function updateAgent(agentName, status) {

    const element = agentElements[agentName];

    if (!element) return;

    const indicator = element.querySelector(".status");

    indicator.classList.remove(
        "waiting",
        "running",
        "completed"
    );

    indicator.classList.add(status);

}

// ======================================================
// STREAM HANDLER
// ======================================================

function handleStreamEvent(data, eventSource) {

    switch (data.type) {

        case "agent_update":

            updateAgent(
                data.agent,
                "completed"
            );

            break;

        case "final_report":

            displayReport(data.report);

            researchButton.disabled = false;

            researchButton.innerHTML = "🔍 Start Research";

            eventSource.close();

            break;

        case "error":

            showPlaceholder(
                "Error",
                data.message
            );

            researchButton.disabled = false;

            researchButton.innerHTML = "🔍 Start Research";

            eventSource.close();

            break;

        default:

            console.log("Unknown Event:", data);

    }

}

// ======================================================
// MAIN FUNCTION
// ======================================================

function startResearch() {

    const query = queryInput.value.trim();

    if (!query) {

        alert("Please enter a research topic.");

        return;

    }

    resetAgents();

    showPlaceholder(
        "Researching...",
        "Our AI agents are working on your request."
    );

    researchButton.disabled = true;

    researchButton.innerHTML = "Researching...";

    const encodedQuery = encodeURIComponent(query);

    const eventSource = new EventSource(
        `${API_URL}/research/stream?query=${encodedQuery}`
    );

    eventSource.onmessage = function (event) {

        const data = JSON.parse(event.data);

        console.log(data);

        handleStreamEvent(
            data,
            eventSource
        );

    };

    eventSource.onerror = function () {

        console.error("Streaming connection failed.");

        showPlaceholder(
            "Connection Lost",
            "Unable to connect to backend."
        );

        researchButton.disabled = false;

        researchButton.innerHTML = "🔍 Start Research";

        eventSource.close();

    };

}

// ======================================================
// EVENT LISTENERS
// ======================================================

researchButton.addEventListener(
    "click",
    startResearch
);

queryInput.addEventListener(
    "keypress",
    function (event) {

        if (event.key === "Enter") {

            startResearch();

        }

    }
);