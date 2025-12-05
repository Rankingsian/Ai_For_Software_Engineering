# Part 3: Ethical Reflection

## Scenario
The predictive model trained in Task 3 (predicting issue priority based on breast cancer data features) is deployed in a company to prioritize software issues or resource allocation.

## 1. Potential Biases in the Dataset

Even technical datasets can harbor hidden biases that lead to unfair outcomes.
*   **Representation Bias:** If the training data (historical issues) comes predominantly from one specific team, region, or demographic of users, the model will overfit to their specific patterns. For example, if "High Priority" issues are historically tagged mostly by senior developers (who might be predominantly male or from a specific region in a global company), the model might learn to associate features of their writing style or code modules with "High Priority," effectively down-ranking critical issues reported by junior developers or underrepresented groups.
*   **Historical Bias:** If the company historically neglected issues from certain legacy systems or specific user bases (e.g., accessibility features), the model will learn that these issues are "Low Priority" and perpetuate this neglect, even if the company's current goals are to improve in those areas.
*   **Labeling Bias:** The "ground truth" (priority labels) was created by humans who have their own subjective biases. If a manager consistently marked UI bugs as "Low Priority" regardless of severity, the AI will encode this preference, potentially leading to a poor user experience.

## 2. Addressing Biases with IBM AI Fairness 360

IBM AI Fairness 360 (AIF360) is an open-source toolkit that can help detect and mitigate these biases throughout the AI lifecycle.

*   **Bias Detection (Pre-processing):** Before training, we can use AIF360 to calculate metrics like **Disparate Impact** or **Statistical Parity Difference**. For instance, we could define "privileged groups" (e.g., issues from the core engineering team) and "unprivileged groups" (e.g., issues from the accessibility team) and check if the "High Priority" label is distributed significantly unevenly between them.
*   **Bias Mitigation (In-processing & Post-processing):**
    *   **Reweighing:** AIF360 can generate weights for the training examples to ensure that unprivileged groups are weighted higher, forcing the model to pay more attention to them during training.
    *   **Adversarial Debiasing:** We could use an adversarial network that tries to predict the sensitive attribute (e.g., which team submitted the issue) from the model's predictions. The main model is penalized if the adversary succeeds, forcing it to make predictions that are independent of the sensitive attribute.
    *   **Calibrated Equality of Odds:** After the model is trained, we can adjust the decision threshold for different groups to ensure that the False Positive and False Negative rates are comparable across groups, ensuring that no team is unfairly penalized by having their critical issues ignored.
