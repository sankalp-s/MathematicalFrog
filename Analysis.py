#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
from typing import List, Tuple
import pandas as pd


class AgenticPipelineAnalyzer:
    
    def __init__(self):
        self.results = {}
    
    def calculate_system_accuracy(self, agent_accuracy: float, num_agents: int) -> float:
        if not (0 < agent_accuracy <= 1):
            raise ValueError("Agent accuracy must be between 0 and 1 (inclusive)")
        if num_agents <= 0:
            raise ValueError("Number of agents must be positive")
        
        return agent_accuracy ** num_agents
    
    def calculate_derivative(self, agent_accuracy: float, num_agents: int) -> float:
        return num_agents * (agent_accuracy ** (num_agents - 1))
    
    def calculate_improvement_gain(self, 
                                   base_accuracy: float, 
                                   improved_accuracy: float, 
                                   num_agents: int) -> dict:
        delta_p = improved_accuracy - base_accuracy
        base_system_acc = self.calculate_system_accuracy(base_accuracy, num_agents)
        improved_system_acc = self.calculate_system_accuracy(improved_accuracy, num_agents)
        absolute_gain = improved_system_acc - base_system_acc
        relative_gain = (absolute_gain / base_system_acc) * 100
        multiplicative_ratio = improved_system_acc / base_system_acc
        theoretical_gain = num_agents * (base_accuracy ** (num_agents - 1)) * delta_p
        
        return {
            'base_system_accuracy': base_system_acc,
            'improved_system_accuracy': improved_system_acc,
            'absolute_gain': absolute_gain,
            'relative_gain_percent': relative_gain,
            'multiplicative_ratio': multiplicative_ratio,
            'theoretical_gain_approx': theoretical_gain,
            'delta_p': delta_p
        }
    
    def demonstrate_exponential_decay(self, 
                                     agent_accuracies: List[float] = [0.9, 0.95, 0.99],
                                     max_agents: int = 10) -> pd.DataFrame:
        results = []
        
        for p in agent_accuracies:
            for n in range(1, max_agents + 1):
                system_acc = self.calculate_system_accuracy(p, n)
                results.append({
                    'agent_accuracy': p,
                    'num_agents': n,
                    'system_accuracy': system_acc,
                    'system_accuracy_percent': system_acc * 100
                })
        
        return pd.DataFrame(results)
    
    def paper_example_section_5(self):
        print("\nSection 5: Numerical Example")
        print("-" * 40)
        
        base_p = 0.90
        improved_p = 0.95
        n = 5
        
        result = self.calculate_improvement_gain(base_p, improved_p, n)
        
        print(f"n = {n}, p = {base_p:.2f}")
        print(f"A(0.90) = 0.90^5 = {result['base_system_accuracy']:.5f}")
        print(f"\nWith feedback: p = {improved_p:.2f}")
        print(f"A(0.95) = 0.95^5 = {result['improved_system_accuracy']:.5f}")
        print(f"\nImprovement: {result['relative_gain_percent']:.2f}%")
        
        return result
    
    def visualize_exponential_decay(self, max_agents: int = 10):
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 5))
        
        accuracies = [0.85, 0.90, 0.95, 0.99]
        colors = ['red', 'orange', 'blue', 'green']
        
        for p, color in zip(accuracies, colors):
            n_values = range(1, max_agents + 1)
            system_accs = [self.calculate_system_accuracy(p, n) for n in n_values]
            ax1.plot(n_values, system_accs, marker='o', label=f'p = {p}', 
                    color=color, linewidth=2)
        
        ax1.set_xlabel('Number of Agents (n)', fontsize=12)
        ax1.set_ylabel('System Accuracy A(p)', fontsize=12)
        ax1.set_title('Exponential Decay: System Accuracy vs Pipeline Depth', 
                     fontsize=14, fontweight='bold')
        ax1.legend()
        ax1.grid(True, alpha=0.3)
        ax1.set_ylim([0, 1])
        
        base_p = 0.90
        improvements = [0.03, 0.05, 0.07, 0.09]
        
        n_values = range(1, max_agents + 1)
        base_accs = [base_p ** n for n in n_values]
        ax2.plot(n_values, base_accs, marker='o', color='gray', 
                linewidth=2, linestyle='--', label=f'No feedback (p = {base_p})')
        
        colors_fb = ['green', 'blue', 'purple', 'red']
        for delta_p, color in zip(improvements, colors_fb):
            improved_p = base_p + delta_p
            improved_accs = [improved_p ** n for n in n_values]
            ax2.plot(n_values, improved_accs, marker='s', color=color,
                    label=f'With feedback: p = {improved_p:.2f} (+{delta_p:.2f})', linewidth=2)
        
        ax2.set_xlabel('Number of Agents (n)', fontsize=12)
        ax2.set_ylabel('System Accuracy', fontsize=12)
        ax2.set_title('System Accuracy With Feedback (base p = 0.90)', 
                     fontsize=14, fontweight='bold')
        ax2.legend()
        ax2.grid(True, alpha=0.3)
        ax2.set_ylim([0, 1])
        
        plt.tight_layout()
        plt.savefig('/Users/sankalpssss/Desktop/RocketFrog/pipeline_analysis_visualization.png', 
                    dpi=300, bbox_inches='tight')
        print("Saved as 'pipeline_analysis_visualization.png'")
        plt.show()
    
    def sensitivity_analysis(self, base_accuracy: float = 0.90, num_agents: int = 5):
        print("\nSensitivity Analysis (n = 5, p = 0.90)")
        print("-" * 40)
        
        improvements = [0.01, 0.02, 0.03, 0.05, 0.10]
        
        for delta_p in improvements:
            new_p = base_accuracy + delta_p
            result = self.calculate_improvement_gain(base_accuracy, new_p, num_agents)
            print(f"Δp = +{delta_p:.2f}: {result['base_system_accuracy']:.5f} → {result['improved_system_accuracy']:.5f} (gain: {result['relative_gain_percent']:.2f}%)")
    
    def compare_strategies(self):
        print("\nStrategy Comparison")
        print("-" * 40)
        
        base_agents = 10
        base_accuracy = 0.90
        base_system = self.calculate_system_accuracy(base_accuracy, base_agents)
        
        print(f"Baseline: n=10, p=0.90 → A={base_system:.5f}")
        
        reduced_agents = 5
        strategy1_system = self.calculate_system_accuracy(base_accuracy, reduced_agents)
        print(f"Strategy 1: n=5, p=0.90 → A={strategy1_system:.5f}")
        
        improved_accuracy = 0.95
        strategy2_system = self.calculate_system_accuracy(improved_accuracy, base_agents)
        print(f"Strategy 2: n=10, p=0.95 → A={strategy2_system:.5f}")


class FeedbackMechanism:
    
    @staticmethod
    def verification_feedback(base_accuracy: float, verification_accuracy: float) -> float:
        return base_accuracy + (1 - base_accuracy) * verification_accuracy
    
    @staticmethod
    def retry_feedback(base_accuracy: float, num_retries: int = 2) -> float:
        return 1 - (1 - base_accuracy) ** num_retries
    
    @staticmethod
    def self_checking_feedback(base_accuracy: float, check_accuracy: float) -> float:
        return base_accuracy + (1 - base_accuracy) * check_accuracy * 0.8
    
    def demonstrate_feedback_mechanisms(self):
        print("\nFeedback Mechanisms (n=5, p=0.90)")
        print("-" * 40)
        
        base_p = 0.90
        num_agents = 5
        base_system = base_p ** num_agents
        
        print(f"Baseline: A = {base_system:.5f}\n")
        
        mechanisms = [
            ("Verification", self.verification_feedback(base_p, 0.95)),
            ("Retry (2x)", self.retry_feedback(base_p, 2)),
            ("Self-check", self.self_checking_feedback(base_p, 0.90)),
            ("Retry (3x)", self.retry_feedback(base_p, 3)),
        ]
        
        for name, improved_p in mechanisms:
            improved_system = improved_p ** num_agents
            print(f"{name}: p'={improved_p:.4f} → A={improved_system:.5f}")


def main():
    print("\nSequential Agentic AI Pipeline Analysis")
    print("="*40)
    
    analyzer = AgenticPipelineAnalyzer()
    
    analyzer.paper_example_section_5()
    
    print("\nExponential Decay")
    print("-" * 40)
    decay_df = analyzer.demonstrate_exponential_decay()
    print(decay_df.head(15).to_string(index=False))
    
    analyzer.sensitivity_analysis(base_accuracy=0.90, num_agents=5)
    analyzer.compare_strategies()
    
    feedback = FeedbackMechanism()
    feedback.demonstrate_feedback_mechanisms()
    
    print("\nGenerating visualization...")
    analyzer.visualize_exponential_decay(max_agents=10)
    print("Done.")


if __name__ == "__main__":
    main()
