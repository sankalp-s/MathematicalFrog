# Sequential Agentic AI Pipeline Reliability Analysis

This repository contains a detailed Python implementation of the mathematical concepts of Improving Reliability in Sequential Agentic AI Pipelines Through Feedback.

## Summary

Analysing how sequential multi-agent AI pipelines suffer from **compounding error** - even when each agent performs with high individual accuracy, the end-to-end system accuracy degrades exponentially with pipeline depth.

### Key Mathematical Concepts

1. **System Accuracy Formula**: `A(p) = p^n`
   - `p` = individual agent accuracy
   - `n` = number of agents in pipeline
   - Result: Exponential decay

2. **Derivative**: `A'(p) = n * p^(n-1)`
   - Shows system accuracy increases with better agents
   - But slope shrinks rapidly as `n` increases

3. **Improvement with Feedback**: `ΔA ≈ n * p^(n-1) * Δp`
   - Small improvements in agent accuracy lead to exponential system gains
   - Multiplicative ratio: `(1 + Δp/p)^n` grows exponentially

## Python Script Features

The script `Analysis.py` provides:

### 1. **AgenticPipelineAnalyzer Class**
- Calculate system accuracy for any pipeline configuration
- Demonstrate exponential decay patterns
- Perform sensitivity analysis
- Compare improvement strategies
- Generate visualizations

### 2. **FeedbackMechanism Class**
Implements various feedback strategies:
- **Verification**: Second agent checks first agent's output
- **Retry**: Multiple attempts if first fails
- **Self-checking**: Agent validates its own output

### 3. **Key Demonstrations**

#### Example
```
Pipeline: 5 agents at 90% accuracy
- Without feedback: 59.05% system accuracy
- With feedback (95%): 77.38% system accuracy
- Result: 31% improvement from just 5-point increase per agent!
```

#### Exponential Decay Visualization
Shows how system accuracy drops as more agents are added, for different accuracy levels.

#### Strategy Comparison
- **Strategy 1**: Reduce number of agents (loses functionality)
- **Strategy 2**: Improve accuracy with feedback (optimal!)


## 📊 Visualizations

1. **Exponential Decay**: System accuracy vs number of agents for different base accuracies
2. **Improvement Ratios**: Shows exponential gains from feedback mechanisms

##  Key Insights

1. **Compounding Error Problem**
   - 90% per agent → only 59% for 5 agents
   - 90% per agent → only 35% for 10 agents

2. **Feedback Solution**
   - Just 5% improvement per agent = 31%+ system improvement
   - Works by raising effective accuracy of each agent

3. **Optimal Strategy**
   - Don't reduce agents (loses capabilities)
   - Improve accuracy via feedback mechanisms:
     - Verification
     - Self-checking
     - Retries
     - Abstention

4. **Mathematical Proof**
   - Feedback is provably optimal for scaling multi-agent systems
   - Small improvements compound exponentially

##  Mathematical Examples

### Example 1: Exponential Decay
```python
# 5 agents at 90% accuracy each
system_accuracy = 0.9 ** 5 = 0.59049 (59%)
```

### Example 2: Feedback Impact
```python
# Improving from 90% to 95% per agent
before = 0.9 ** 5 = 0.59049
after = 0.95 ** 5 = 0.77378
improvement = 31.04%
```

### Example 3: Sensitivity
```python
# 5 agents, base 90%
+1% per agent → +5.7% system improvement
+2% per agent → +11.6% system improvement
+5% per agent → +31.0% system improvement
```
