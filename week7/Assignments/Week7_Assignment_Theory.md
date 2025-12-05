# Week 7 Assignment: AI Ethics and Policy

## Part 1: Theoretical Understanding (30%)

### 1. Short Answer Questions

**Q1: Define algorithmic bias and provide two examples of how it manifests in AI systems.**

**Definition:** Algorithmic bias refers to systematic and repeatable errors in a computer system that create unfair outcomes, such as privileging one arbitrary group of users over others. It often stems from biased training data, flawed model assumptions, or lack of diversity in the development team.

**Examples:**
1.  **Hiring Algorithms:** An AI tool trained on resumes of past successful employees (mostly men) might downgrade resumes containing the word "women's" (e.g., "women's chess club"), as seen in Amazon's scrapped recruiting tool.
2.  **Healthcare Risk Prediction:** An algorithm used to allocate health care to patients found that Black patients had to be much sicker than White patients to be recommended for the same care, because the model used health costs as a proxy for health needs, and less money was spent on Black patients who had the same level of need.

**Q2: Explain the difference between transparency and explainability in AI. Why are both important?**

*   **Transparency** relates to the openness about the AI system's existence, its data sources, its development process, and its purpose. It answers "What is this system, who built it, and what data does it use?"
*   **Explainability** (or Interpretability) refers to the ability to understand *how* the model arrived at a specific decision. It answers "Why did the model make this specific prediction?"

**Importance:** Both are crucial for trust and accountability. Transparency allows for external auditing and informed consent. Explainability is essential for debugging, detecting bias, and providing recourse to individuals affected by automated decisions (e.g., knowing why a loan was denied).

**Q3: How does GDPR (General Data Protection Regulation) impact AI development in the EU?**

The GDPR significantly impacts AI by:
1.  **Right to Explanation (Article 22):** Individuals have the right not to be subject to a decision based solely on automated processing which produces legal effects, and they can request an explanation for such decisions.
2.  **Data Minimization:** AI developers must only collect data that is necessary for the specific purpose, challenging the "collect everything" approach of deep learning.
3.  **Consent:** Explicit and informed consent is required for data processing, and users have the right to withdraw it.
4.  **Bias and Fairness:** The requirement for fair processing implies that AI systems must be tested for and cleansed of discriminatory bias.

### 2. Ethical Principles Matching

*   **Ensuring AI does not harm individuals or society:** B) Non-maleficence
*   **Respecting users’ right to control their data and decisions:** C) Autonomy
*   **Designing AI to be environmentally friendly:** D) Sustainability
*   **Fair distribution of AI benefits and risks:** A) Justice

---

## Part 2: Case Study Analysis (40%)

### Case 1: Biased Hiring Tool

**Scenario:** Amazon’s AI recruiting tool penalized female candidates.

**Tasks:**

1.  **Identify the source of bias:**
    *   The primary source was the **training data**. The model was trained on resumes submitted to the company over a 10-year period. Since the tech industry has historically been male-dominated, the data reflected this imbalance. The model learned that "male" patterns (or lack of "female" keywords) correlated with successful hiring, effectively teaching itself that male candidates were preferable.

2.  **Propose three fixes to make the tool fairer:**
    *   **Data Balancing & Augmentation:** Re-sample the training data to ensure equal representation of male and female candidates, or use synthetic data techniques to augment the underrepresented class.
    *   **Feature Engineering/Blindness:** Explicitly remove gender-identifying terms (e.g., "women's", "softball") and proxies from the input features. However, one must be careful of hidden proxies.
    *   **Regular Bias Auditing:** Implement a continuous monitoring loop where the model's output is regularly tested against fairness metrics (like demographic parity) before and after deployment.

3.  **Suggest metrics to evaluate fairness post-correction:**
    *   **Disparate Impact Ratio:** Comparing the selection rate of female candidates vs. male candidates. A ratio close to 1 indicates fairness.
    *   **Equal Opportunity Difference:** Ensuring that the True Positive Rates are similar for both groups (i.e., qualified women are selected at the same rate as qualified men).

### Case 2: Facial Recognition in Policing

**Scenario:** A facial recognition system misidentifies minorities at higher rates.

**Tasks:**

1.  **Discuss ethical risks:**
    *   **Wrongful Arrests:** Higher false positive rates for minorities can lead to innocent individuals being detained, questioned, or arrested, causing psychological trauma and reputational damage.
    *   **Reinforcing Systemic Racism:** If deployed in already over-policed communities, biased tools exacerbate existing inequalities and erode trust in law enforcement.
    *   **Privacy Violations:** Mass surveillance without consent infringes on the right to anonymity and freedom of movement.

2.  **Recommend policies for responsible deployment:**
    *   **Human-in-the-Loop Requirement:** Facial recognition matches should never automatically trigger an arrest. They must be treated as a lead requiring independent human verification.
    *   **Mandatory Accuracy Testing:** Before deployment, systems must pass rigorous independent testing across all demographic groups (race, gender, age) with strict accuracy thresholds.
    *   **Restricted Use Cases:** Ban the use of real-time facial recognition in public spaces for general surveillance. Limit its use to investigating serious crimes with a judicial warrant.

---

## Part 4: Ethical Reflection (5%)

**Prompt:** Reflect on a personal project (past or future). How will you ensure it adheres to ethical AI principles?

**Reflection:**
In a future project designing a **Personalized Learning Assistant for Students**, I would prioritize **Autonomy** and **Justice**.
To ensure **Autonomy**, I would design the system to be a "nudge" rather than a dictator. The AI would suggest study schedules or topics, but the student would always have the final say and the ability to override recommendations. I would also ensure transparency by showing *why* a certain topic was recommended (e.g., "You missed similar questions in the last quiz").
To ensure **Justice**, I would be vigilant about the training data. If the model is trained on data from students in wealthy schools, it might set unrealistic standards or bias content recommendations against students from different backgrounds. I would audit the system to ensure it performs equally well for students of different learning abilities and socio-economic backgrounds, ensuring it doesn't leave anyone behind.

---

## Bonus Task: Policy Proposal (Extra 10%)

### Guideline for Ethical AI Use in Healthcare

**Objective:** To ensure AI systems in healthcare improve patient outcomes without compromising safety, privacy, or equity.

**1. Patient Consent Protocols**
*   **Informed Consent:** Patients must be explicitly informed if an AI system is being used to aid in their diagnosis or treatment plan.
*   **Opt-Out Mechanism:** Patients should have the right to request a human-only review of their case, especially for critical life-altering decisions.
*   **Data Usage:** Clear, simplified explanations must be provided regarding how patient data will be used to train or fine-tune models, with strict adherence to de-identification standards.

**2. Bias Mitigation Strategies**
*   **Representative Data:** AI models must be trained on diverse datasets that accurately reflect the demographics of the patient population they will serve (age, race, gender, comorbidities).
*   **Pre-Deployment Audits:** All models must undergo a "fairness audit" to check for performance disparities across different demographic groups before clinical rollout.
*   **Continuous Monitoring:** Real-world performance must be monitored to detect "drift" or emerging biases that weren't present during testing.

**3. Transparency Requirements**
*   **Model Cards:** Every deployed AI system must have a "Model Card" accessible to clinicians, detailing its intended use, limitations, training data sources, and known performance characteristics.
*   **Explainability:** Clinical decision support systems should provide confidence scores and, where possible, feature importance (e.g., "Flagged for sepsis risk due to rising heart rate and low blood pressure") to aid clinician judgment.
*   **Accountability:** It must be clearly defined that the ultimate responsibility for medical decisions lies with the human clinician, with the AI serving as an assistive tool.
