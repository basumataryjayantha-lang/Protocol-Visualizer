
<script>

let applicationEvents = [];
let transportEvents = [];

let currentStep = 0;
let currentView = "application";
let timer = null;


// ================================
// START ACTIVITY
// ================================

async function startActivity(activity) {

    currentStep = 0;

    pauseSimulation();

    document.getElementById("statusText").innerText =
        "Loading " + activity + "...";

    try {

        const response = await fetch(
            "/simulate",
            {
                method: "POST",

                headers: {
                    "Content-Type": "application/json"
                },

                body: JSON.stringify({
                    activity: activity
                })
            }
        );

        const data = await response.json();

        applicationEvents = data.application;
        transportEvents = data.transport;

        document.getElementById("statusText").innerText =
            activity.toUpperCase() + " simulation started.";

        renderCurrentStep();

    }

    catch (error) {

        console.error(error);

        document.getElementById("statusText").innerText =
            "Error: " + error.message;
    }
}


// ================================
// SWITCH VIEW
// ================================

function switchView(view) {

    currentView = view;

    renderCurrentStep();
}


// ================================
// RENDER CURRENT STEP
// ================================

function renderCurrentStep() {

    if (currentView === "application") {

        renderApplication();

    }

    else {

        renderTransport();

    }
}


// ================================
// APPLICATION LAYER
// ================================

function renderApplication() {

    const area =
        document.getElementById("visualization");

    if (applicationEvents.length === 0) {

        area.innerHTML = `
            <h2>No Events</h2>
        `;

        return;
    }

    const index = Math.min(
        currentStep,
        applicationEvents.length - 1
    );

    const event = applicationEvents[index];

    document.getElementById("stepIndicator").innerText =
        "Application Step " +
        (currentStep + 1) +
        " / " +
        applicationEvents.length;

    area.innerHTML = `

        <h2>${event.protocol}</h2>

        <h3>${event.message}</h3>

        <p>
            <strong>Direction:</strong>
            ${event.direction}
        </p>

        <p>
            ${event.description}
        </p>

        <hr>

        <p>
            <strong>Timeline Step:</strong>
            ${currentStep + 1}
        </p>

    `;
}


// ================================
// TRANSPORT LAYER
// ================================

function renderTransport() {

    const area =
        document.getElementById("visualization");

    if (transportEvents.length === 0) {

        area.innerHTML = `
            <h2>No Transport Events</h2>
        `;

        return;
    }

    const index = Math.min(
        currentStep,
        transportEvents.length - 1
    );

    const event = transportEvents[index];

    document.getElementById("stepIndicator").innerText =
        "Transport Step " +
        (currentStep + 1) +
        " / " +
        transportEvents.length;

    area.innerHTML = `

        <h2>
            TCP ${event.type}
        </h2>

        <h3>
            ${event.direction}
        </h3>

        <hr>

        <p>
            <strong>Seq:</strong>
            ${event.seq}
        </p>

        <p>
            <strong>Ack:</strong>
            ${event.ack}
        </p>

        <p>
            <strong>Window:</strong>
            ${event.window}
        </p>

        <p>
            <strong>Flags:</strong>
            ${event.flags}
        </p>

        <p>
            <strong>Length:</strong>
            ${event.length}
        </p>

        <p>
            <strong>TCP State:</strong>
            ${event.state}
        </p>

        <hr>

        <p>
            <strong>Timeline Step:</strong>
            ${currentStep + 1}
        </p>

    `;
}


// ================================
// NEXT
// ================================

function nextStep() {

    const maxSteps = Math.max(
        applicationEvents.length,
        transportEvents.length
    );

    if (currentStep < maxSteps - 1) {

        currentStep++;

        renderCurrentStep();
    }
}


// ================================
// PREVIOUS
// ================================

function previousStep() {

    if (currentStep > 0) {

        currentStep--;

        renderCurrentStep();
    }
}


// ================================
// PLAY
// ================================

function playSimulation() {

    if (timer !== null) {

        return;
    }

    timer = setInterval(
        function () {

            const maxSteps = Math.max(
                applicationEvents.length,
                transportEvents.length
            );

            if (currentStep >= maxSteps - 1) {

                pauseSimulation();

                return;
            }

            currentStep++;

            renderCurrentStep();

        },
        1500
    );
}


// ================================
// PAUSE
// ================================

function pauseSimulation() {

    if (timer !== null) {

        clearInterval(timer);

        timer = null;
    }
}


// ================================
// REPLAY
// ================================

function replaySimulation() {

    pauseSimulation();

    currentStep = 0;

    renderCurrentStep();
}

</script>
