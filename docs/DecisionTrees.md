## Decision Trees

---

- Decision Trees are greedy
- Goal is to minimize impurity across the derived nodes
- $Criterion = f(parent) - \Sigma w_i f(child_i)$

---

- For **Classification** Trees
- Choose splits that maximize **Information Gain**
- f can be either Entropy or Gini Index
- **Entropy**
- $Entropy = \Sigma -p_i * \log_2(p_i)\, \forall \, i\,\in classes$
- Entropy will be take the max value of 1 if classes are equal
- **Gini Index**
- $GI = 1 - \Sigma pi^2 \, \forall \, i\,\in classes$

---

- For **Regression** Trees
- Choose split that maximize **Variance Reduction**
- f will typically be
- $Var = \Sigma \, \dfrac{1}{n} \, (y_i - \hat y)^2$
