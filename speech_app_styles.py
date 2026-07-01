custom_css = """
/* Background */
.gradio-container {
    background: #F8F5FF;
    font-family: 'Segoe UI', sans-serif;
}

/* Hero Section */
.hero {
    background: linear-gradient(135deg, #7C3AED, #A855F7, #EC4899);
    color: white;
    border-radius: 22px;
    padding: 35px;
    text-align: center;
    margin-bottom: 20px;
    box-shadow: 0 10px 25px rgba(0,0,0,.15);
}

.hero h1 {
    font-size: 38px;
    margin-bottom: 8px;
}

.hero p {
    font-size: 18px;
    opacity: .95;
}

/* Cards & Layout Panels */
.card {
    background: white;
    border-radius: 20px;
    padding: 25px;
    box-shadow: 0 5px 18px rgba(0,0,0,.08);
}

.side-card {
    background: white;
    border-radius: 20px;
    padding: 20px;
    box-shadow: 0 8px 20px rgba(0,0,0,.08);
}

.side-panel h2 {
    color: #7C3AED;
    margin-bottom: 15px;
}

.languages {
    background: white;
    border-radius: 20px;
    padding: 20px;
    margin-top: 20px;
    box-shadow: 0 5px 18px rgba(0,0,0,.08);
}

.languages h3 {
    color: #7C3AED;
    margin-bottom: 15px;
}

/* Buttons */
button {
    border-radius: 12px !important;
    transition: .3s;
}

button:hover {
    transform: translateY(-2px);
}

/* Chips & Lists */
.chip-container {
    display: flex;
    flex-wrap: wrap;
    gap: 12px;
    justify-content: center;
}

.chip {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background: #F3E8FF;
    color: #6D28D9;
    padding: 10px 18px;
    border-radius: 25px;
    font-weight: 600;
    font-size: 15px;
    border: 1px solid #D8B4FE;
    transition: all 0.3s ease;
    cursor: default;
}

.chip:hover {
    background: linear-gradient(135deg, #7C3AED, #EC4899);
    color: white;
    transform: translateY(-3px) scale(1.03);
    box-shadow: 0 8px 20px rgba(124, 58, 237, 0.3);
}

.feature-list {
    list-style: none;
    padding: 0;
}

.feature-list li {
    background: #F3E8FF;
    margin: 10px 0;
    padding: 12px;
    border-radius: 12px;
    color: #4C1D95;
    font-weight: 600;
    transition: .3s;
}

.feature-list li:hover {
    background: #7C3AED;
    color: white;
}

/* Character & Word Counter */
.counter {
    color: #7C3AED;
    font-size: 15px;
    font-weight: 600;
    padding: 5px 0;
}

/* Structural Elements */
hr {
    margin: 25px 0;
    border: 1px solid #E9D5FF;
}

.footer {
    text-align: center;
    color: #666;
    margin-top: 25px;
    font-size: 14px;
}

/* ===========================
   Status Messages (HTML Fixes)
=========================== */
.status-message {
    padding: 12px;
    margin-top: 10px;
    border-radius: 10px;
    font-size: 16px;
    font-weight: 600;
    display: block;
}

.success {
    background: #ECFDF5 !important;
    color: #6D28D9 !important;
    border: 1px solid #10B981;
}

.error {
    background: #FEF2F2 !important;
    color: #4C1D95 !important;
    border: 1px solid #EF4444;
}
"""