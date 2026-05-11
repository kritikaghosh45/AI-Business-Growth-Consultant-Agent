import json
import textwrap

class GrowthConsultantAgent:
    """A simple agent that generates business growth recommendations."""

    def __init__(self, profile: dict):
        self.profile = profile

    def analyze_business_profile(self) -> dict:
        strategy = self._build_strategy()
        marketing = self._build_marketing_plan()
        product = self._build_product_plan()
        operations = self._build_operations_plan()

        return {
            "strategy": strategy,
            "marketing": marketing,
            "product": product,
            "operations": operations,
        }

    def _build_strategy(self) -> dict:
        revenue = self.profile.get("annual_revenue_million", 0)
        goals = self.profile.get("growth_goals", "").strip()
        position = self.profile.get("industry", "").lower()
        segments = self.profile.get("customers", "").lower()

        strategy = {
            "focus": "Accelerate recurring revenue and market expansion.",
            "priority": "High",
            "recommendations": [],
        }

        if revenue < 5:
            strategy["recommendations"].append(
                "Strengthen revenue predictability with subscription or service contracts."
            )
        else:
            strategy["recommendations"].append(
                "Invest in scalable demand generation to support rapid expansion."
            )

        if "renewable" in position or "energy" in position:
            strategy["recommendations"].append(
                "Position the brand around sustainability and long-term cost savings."
            )

        if "regional" in goals or "new markets" in goals:
            strategy["recommendations"].append(
                "Use a market prioritization matrix to enter the most profitable regions first."
            )

        if "commercial" in segments:
            strategy["recommendations"].append(
                "Create tailored enterprise offers for commercial decision makers."
            )

        return strategy

    def _build_marketing_plan(self) -> dict:
        channels = self.profile.get("primary_channels", [])
        strengths = self.profile.get("strengths", [])
        weaknesses = self.profile.get("weaknesses", [])

        marketing = {
            "focus_areas": [],
            "recommended_channels": [],
            "quick_wins": [],
        }

        if "digital marketing" in channels or "social media" in channels:
            marketing["recommended_channels"].append(
                "Content marketing focused on case studies, ROI, and trust building."
            )
        else:
            marketing["recommended_channels"].append(
                "Add digital demand-generation channels to improve lead volume."
            )

        if "industry events" in channels:
            marketing["recommended_channels"].append(
                "Leverage industry conferences to showcase customer success stories."
            )

        if "low brand awareness" in weaknesses:
            marketing["quick_wins"].append(
                "Publish three flagship case studies and promote them via email and LinkedIn."
            )

        if "strong engineering team" in strengths:
            marketing["quick_wins"].append(
                "Use technical credibility to launch a webinar series for qualified prospects."
            )

        marketing["focus_areas"].append("Demand generation")
        marketing["focus_areas"].append("Brand positioning")
        return marketing

    def _build_product_plan(self) -> dict:
        products = {
            "improvements": [],
            "differentiators": [],
            "recommendations": [],
        }

        if self.profile.get("weaknesses"):
            products["recommendations"].append(
                "Automate onboarding to reduce friction and improve customer satisfaction."
            )

        if self.profile.get("strengths"):
            products["differentiators"].append(
                "Highlight the proven engineering and installation expertise in product messaging."
            )

        products["improvements"].append(
            "Develop a service package that includes post-sale monitoring and maintenance."
        )

        return products

    def _build_operations_plan(self) -> dict:
        operations = {
            "efficiency_actions": [],
            "resourcing_actions": [],
            "technology_actions": [],
        }

        operations["efficiency_actions"].append(
            "Document the customer journey and reduce manual handoffs."
        )
        operations["technology_actions"].append(
            "Add CRM automation for lead tracking and contract renewals."
        )

        if self.profile.get("annual_revenue_million", 0) < 10:
            operations["resourcing_actions"].append(
                "Hire or contract a growth marketer to focus on repeatable campaigns."
            )

        return operations

    def generate_report(self) -> str:
        analysis = self.analyze_business_profile()
        lines = [f"Business Growth Plan for {self.profile.get('company_name', 'Your Business')}", "=" * 50, ""]

        for section, details in analysis.items():
            lines.append(section.capitalize())
            lines.append("-" * len(section))
            lines.extend(self._format_section(details))
            lines.append("")

        return "\n".join(lines)

    @staticmethod
    def _format_section(details: dict) -> list[str]:
        text_lines = []
        for key, value in details.items():
            if isinstance(value, list):
                text_lines.append(f"{key.replace('_', ' ').capitalize()}:")
                for item in value:
                    text_lines.append(f"  - {item}")
            else:
                text_lines.append(f"{key.replace('_', ' ').capitalize()}: {value}")
        return text_lines


def load_sample_profile() -> dict:
    return {
        "company_name": "SolarVue",
        "industry": "renewable energy",
        "annual_revenue_million": 4.8,
        "growth_goals": "increase recurring revenue and enter two new regional markets",
        "customers": "mid-market commercial property owners",
        "primary_channels": ["direct sales", "industry events", "digital marketing"],
        "strengths": ["strong engineering team", "proven installation process"],
        "weaknesses": ["low brand awareness", "manual customer onboarding"],
    }


def main() -> None:
    print("AI Business Growth Consultant Agent")
    print("====================================")
    print("Choose an option:")
    print("1. Use sample business profile")
    print("2. Enter a custom profile JSON file path")

    choice = input("Select 1 or 2: ").strip()
    if choice == "2":
        path = input("Enter path to JSON profile file: ").strip()
        try:
            with open(path, "r", encoding="utf-8") as f:
                profile = json.load(f)
        except Exception as exc:
            print(f"Failed to read profile: {exc}")
            return
    else:
        profile = load_sample_profile()

    agent = GrowthConsultantAgent(profile)
    report = agent.generate_report()
    print("\n" + report)

    output_path = "growth_plan.txt"
    with open(output_path, "w", encoding="utf-8") as out_file:
        out_file.write(report)

    print(f"\nGenerated growth plan saved to {output_path}")


if __name__ == "__main__":
    main()
