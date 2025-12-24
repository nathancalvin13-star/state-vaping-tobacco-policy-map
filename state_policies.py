"""
State Vaping and Tobacco Policy Database

Comprehensive database of all 50 states' policies on vaping and flavored tobacco products.
Data compiled from Truth Initiative, Campaign for Tobacco-Free Kids, Tax Foundation,
CDC, FDA, and state legislative sources.

Last Updated: December 2024/January 2025
"""

from dataclasses import dataclass, field, asdict
from typing import Optional, List, Dict
import json
from datetime import date


@dataclass
class StateTobaccoPolicy:
    """Comprehensive tobacco and vaping policy data for a state"""

    # Basic info
    state: str
    state_abbr: str

    # Flavored product restrictions
    flavored_ecig_ban: str  # "comprehensive", "partial", "none"
    flavored_ecig_details: str
    flavored_ecig_effective_date: Optional[str] = None

    menthol_cig_ban: bool = False
    menthol_ban_details: str = ""
    menthol_effective_date: Optional[str] = None

    # Taxation
    has_ecig_tax: bool = False
    ecig_tax_rate: str = ""
    ecig_tax_structure: str = ""  # "wholesale %", "per mL", "retail %", "per cartridge"

    # Indoor restrictions
    indoor_vaping_ban: bool = False
    indoor_ban_details: str = ""

    # Age restrictions (federal T21 applies to all)
    minimum_age: int = 21
    state_t21_law: bool = False  # Whether state has own T21 law

    # Additional restrictions
    licensing_required: bool = False
    license_fee: str = ""

    # Notable local restrictions
    local_restrictions: List[str] = field(default_factory=list)

    # Recent policy changes
    recent_changes: str = ""

    # Data sources
    sources: List[str] = field(default_factory=list)

    def to_dict(self) -> Dict:
        """Convert to dictionary for JSON export"""
        return asdict(self)


# State policy database
STATES = [
    StateTobaccoPolicy(
        state="Alabama",
        state_abbr="AL",
        flavored_ecig_ban="none",
        flavored_ecig_details="No statewide restrictions on flavored e-cigarettes",
        has_ecig_tax=False,
        indoor_vaping_ban=False,
        state_t21_law=False,
        sources=["Tax Foundation 2025", "Truth Initiative 2025"]
    ),

    StateTobaccoPolicy(
        state="Alaska",
        state_abbr="AK",
        flavored_ecig_ban="none",
        flavored_ecig_details="No statewide restrictions on flavored e-cigarettes",
        has_ecig_tax=False,
        ecig_tax_rate="No statewide tax, but several municipalities impose taxes: Juneau (45%), Anchorage (55%), Matanuska-Susitna (55%)",
        indoor_vaping_ban=False,
        state_t21_law=True,
        sources=["Tax Foundation 2025", "ComplyIQ 2025"]
    ),

    StateTobaccoPolicy(
        state="Arizona",
        state_abbr="AZ",
        flavored_ecig_ban="none",
        flavored_ecig_details="No statewide restrictions on flavored e-cigarettes",
        has_ecig_tax=False,
        indoor_vaping_ban=False,
        state_t21_law=True,
        sources=["Tax Foundation 2025", "Truth Initiative 2025"]
    ),

    StateTobaccoPolicy(
        state="Arkansas",
        state_abbr="AR",
        flavored_ecig_ban="none",
        flavored_ecig_details="No statewide restrictions on flavored e-cigarettes",
        has_ecig_tax=False,
        indoor_vaping_ban=False,
        state_t21_law=True,
        sources=["Tax Foundation 2025"]
    ),

    StateTobaccoPolicy(
        state="California",
        state_abbr="CA",
        flavored_ecig_ban="comprehensive",
        flavored_ecig_details="Comprehensive ban on all flavored tobacco products including menthol. Voters upheld the ban in November 2022.",
        flavored_ecig_effective_date="2022-12-21",
        menthol_cig_ban=True,
        menthol_ban_details="Statewide ban on menthol cigarettes, approved by voters in 2022",
        menthol_effective_date="2022-12-21",
        has_ecig_tax=True,
        ecig_tax_rate="12.5% wholesale, rising to 56.67% by July 1, 2026",
        ecig_tax_structure="wholesale %",
        indoor_vaping_ban=True,
        indoor_ban_details="Comprehensive smoke-free law covering e-cigarettes in workplaces, restaurants, and bars",
        state_t21_law=True,
        recent_changes="As of Jan 1, 2025, flavor prohibition extended to internet sales. AB 3218 prohibits menthol-like cooling sensations (WS-3, WS-23). SB 1230 allows seizure of illegal flavored products.",
        local_restrictions=["Numerous cities and counties with additional restrictions"],
        sources=["Campaign for Tobacco-Free Kids 2024", "VapeRanger 2025", "Truth Initiative 2025"]
    ),

    StateTobaccoPolicy(
        state="Colorado",
        state_abbr="CO",
        flavored_ecig_ban="partial",
        flavored_ecig_details="State law bans flavored vape products except tobacco and menthol flavors",
        has_ecig_tax=True,
        ecig_tax_rate="30% wholesale (open), 50% wholesale (closed)",
        ecig_tax_structure="wholesale %",
        indoor_vaping_ban=True,
        indoor_ban_details="Comprehensive smoke-free law covering e-cigarettes",
        state_t21_law=True,
        sources=["Tax Foundation 2025", "VapeRanger 2025"]
    ),

    StateTobaccoPolicy(
        state="Connecticut",
        state_abbr="CT",
        flavored_ecig_ban="none",
        flavored_ecig_details="No statewide flavor ban",
        has_ecig_tax=True,
        ecig_tax_rate="$0.40 per mL",
        ecig_tax_structure="per mL",
        indoor_vaping_ban=True,
        indoor_ban_details="Comprehensive smoke-free law covering e-cigarettes",
        state_t21_law=True,
        sources=["Tax Foundation 2025", "Truth Initiative 2025"]
    ),

    StateTobaccoPolicy(
        state="Delaware",
        state_abbr="DE",
        flavored_ecig_ban="partial",
        flavored_ecig_details="Illegal to sell flavored single-use disposable vapes",
        has_ecig_tax=True,
        ecig_tax_rate="$1.25 per mL",
        ecig_tax_structure="per mL",
        indoor_vaping_ban=True,
        indoor_ban_details="Comprehensive smoke-free law covering e-cigarettes",
        licensing_required=True,
        license_fee="$800/year",
        state_t21_law=True,
        sources=["Tax Foundation 2025", "Ecigator 2025", "Truth Initiative 2025"]
    ),

    StateTobaccoPolicy(
        state="Florida",
        state_abbr="FL",
        flavored_ecig_ban="none",
        flavored_ecig_details="No statewide restrictions on flavored e-cigarettes",
        has_ecig_tax=False,
        indoor_vaping_ban=False,
        state_t21_law=False,
        sources=["Tax Foundation 2025"]
    ),

    StateTobaccoPolicy(
        state="Georgia",
        state_abbr="GA",
        flavored_ecig_ban="none",
        flavored_ecig_details="No statewide restrictions on flavored e-cigarettes",
        has_ecig_tax=True,
        ecig_tax_rate="7% wholesale",
        ecig_tax_structure="wholesale %",
        indoor_vaping_ban=False,
        state_t21_law=True,
        sources=["Tax Foundation 2025"]
    ),

    StateTobaccoPolicy(
        state="Hawaii",
        state_abbr="HI",
        flavored_ecig_ban="none",
        flavored_ecig_details="No statewide flavor ban",
        has_ecig_tax=True,
        ecig_tax_rate="70% wholesale",
        ecig_tax_structure="wholesale %",
        indoor_vaping_ban=True,
        indoor_ban_details="Comprehensive smoke-free law covering e-cigarettes",
        state_t21_law=True,
        sources=["Tax Foundation 2025", "Truth Initiative 2025"]
    ),

    StateTobaccoPolicy(
        state="Idaho",
        state_abbr="ID",
        flavored_ecig_ban="none",
        flavored_ecig_details="No statewide restrictions on flavored e-cigarettes",
        has_ecig_tax=False,
        indoor_vaping_ban=False,
        state_t21_law=False,
        sources=["Tax Foundation 2025"]
    ),

    StateTobaccoPolicy(
        state="Illinois",
        state_abbr="IL",
        flavored_ecig_ban="none",
        flavored_ecig_details="No statewide flavor ban, but many local restrictions",
        has_ecig_tax=True,
        ecig_tax_rate="$2.50 per mL",
        ecig_tax_structure="per mL",
        indoor_vaping_ban=True,
        indoor_ban_details="Comprehensive smoke-free law covering e-cigarettes",
        licensing_required=True,
        license_fee="$1,200/year",
        state_t21_law=True,
        local_restrictions=["Chicago has comprehensive local flavor restrictions"],
        sources=["Tax Foundation 2025", "Ecigator 2025", "Truth Initiative 2025"]
    ),

    StateTobaccoPolicy(
        state="Indiana",
        state_abbr="IN",
        flavored_ecig_ban="none",
        flavored_ecig_details="No statewide restrictions on flavored e-cigarettes",
        has_ecig_tax=True,
        ecig_tax_rate="15% wholesale",
        ecig_tax_structure="wholesale %",
        indoor_vaping_ban=False,
        state_t21_law=True,
        sources=["Tax Foundation 2025"]
    ),

    StateTobaccoPolicy(
        state="Iowa",
        state_abbr="IA",
        flavored_ecig_ban="none",
        flavored_ecig_details="No statewide restrictions on flavored e-cigarettes",
        has_ecig_tax=False,
        ecig_tax_rate="Subject to sales tax only",
        indoor_vaping_ban=False,
        state_t21_law=False,
        sources=["Tax Foundation 2025", "ComplyIQ 2025"]
    ),

    StateTobaccoPolicy(
        state="Kansas",
        state_abbr="KS",
        flavored_ecig_ban="none",
        flavored_ecig_details="No statewide restrictions on flavored e-cigarettes",
        has_ecig_tax=True,
        ecig_tax_rate="20% retail",
        ecig_tax_structure="retail %",
        indoor_vaping_ban=True,
        indoor_ban_details="Comprehensive smoke-free law covering e-cigarettes",
        state_t21_law=True,
        sources=["Tax Foundation 2025", "Truth Initiative 2025"]
    ),

    StateTobaccoPolicy(
        state="Kentucky",
        state_abbr="KY",
        flavored_ecig_ban="none",
        flavored_ecig_details="No statewide restrictions on flavored e-cigarettes",
        has_ecig_tax=True,
        ecig_tax_rate="$1.50 per cartridge",
        ecig_tax_structure="per cartridge",
        indoor_vaping_ban=False,
        state_t21_law=True,
        sources=["Tax Foundation 2025"]
    ),

    StateTobaccoPolicy(
        state="Louisiana",
        state_abbr="LA",
        flavored_ecig_ban="none",
        flavored_ecig_details="No statewide restrictions on flavored e-cigarettes",
        has_ecig_tax=True,
        ecig_tax_rate="15% wholesale",
        ecig_tax_structure="wholesale %",
        indoor_vaping_ban=False,
        state_t21_law=True,
        sources=["Tax Foundation 2025"]
    ),

    StateTobaccoPolicy(
        state="Maine",
        state_abbr="ME",
        flavored_ecig_ban="none",
        flavored_ecig_details="No statewide flavor ban",
        has_ecig_tax=True,
        ecig_tax_rate="43% wholesale",
        ecig_tax_structure="wholesale %",
        indoor_vaping_ban=True,
        indoor_ban_details="Comprehensive smoke-free law covering e-cigarettes",
        state_t21_law=True,
        sources=["Tax Foundation 2025", "Truth Initiative 2025"]
    ),

    StateTobaccoPolicy(
        state="Maryland",
        state_abbr="MD",
        flavored_ecig_ban="partial",
        flavored_ecig_details="Limits flavored product sales to age-restricted venues",
        has_ecig_tax=True,
        ecig_tax_rate="60% retail",
        ecig_tax_structure="retail %",
        indoor_vaping_ban=True,
        indoor_ban_details="Comprehensive smoke-free law covering e-cigarettes",
        state_t21_law=True,
        sources=["Tax Foundation 2025", "Ecigator 2025", "Truth Initiative 2025"]
    ),

    StateTobaccoPolicy(
        state="Massachusetts",
        state_abbr="MA",
        flavored_ecig_ban="comprehensive",
        flavored_ecig_details="First state to ban all flavored tobacco products including menthol cigarettes (effective 2020)",
        flavored_ecig_effective_date="2020-06-01",
        menthol_cig_ban=True,
        menthol_ban_details="Comprehensive ban on menthol cigarettes statewide",
        menthol_effective_date="2020-06-01",
        has_ecig_tax=True,
        ecig_tax_rate="75% wholesale",
        ecig_tax_structure="wholesale %",
        indoor_vaping_ban=True,
        indoor_ban_details="Comprehensive smoke-free law covering e-cigarettes",
        state_t21_law=True,
        sources=["Campaign for Tobacco-Free Kids 2024", "Tax Foundation 2025", "Stateline 2024"]
    ),

    StateTobaccoPolicy(
        state="Michigan",
        state_abbr="MI",
        flavored_ecig_ban="none",
        flavored_ecig_details="No statewide restrictions on flavored e-cigarettes",
        has_ecig_tax=False,
        indoor_vaping_ban=False,
        state_t21_law=True,
        sources=["Tax Foundation 2025"]
    ),

    StateTobaccoPolicy(
        state="Minnesota",
        state_abbr="MN",
        flavored_ecig_ban="none",
        flavored_ecig_details="No statewide flavor ban",
        has_ecig_tax=True,
        ecig_tax_rate="95% wholesale",
        ecig_tax_structure="wholesale %",
        indoor_vaping_ban=False,
        state_t21_law=True,
        sources=["Tax Foundation 2025"]
    ),

    StateTobaccoPolicy(
        state="Mississippi",
        state_abbr="MS",
        flavored_ecig_ban="none",
        flavored_ecig_details="No statewide restrictions on flavored e-cigarettes",
        has_ecig_tax=False,
        indoor_vaping_ban=False,
        state_t21_law=False,
        sources=["Tax Foundation 2025"]
    ),

    StateTobaccoPolicy(
        state="Missouri",
        state_abbr="MO",
        flavored_ecig_ban="none",
        flavored_ecig_details="No statewide restrictions on flavored e-cigarettes",
        has_ecig_tax=False,
        indoor_vaping_ban=False,
        state_t21_law=False,
        sources=["Tax Foundation 2025"]
    ),

    StateTobaccoPolicy(
        state="Montana",
        state_abbr="MT",
        flavored_ecig_ban="none",
        flavored_ecig_details="No statewide restrictions on flavored e-cigarettes",
        has_ecig_tax=False,
        indoor_vaping_ban=False,
        state_t21_law=False,
        sources=["Tax Foundation 2025"]
    ),

    StateTobaccoPolicy(
        state="Nebraska",
        state_abbr="NE",
        flavored_ecig_ban="none",
        flavored_ecig_details="No statewide restrictions on flavored e-cigarettes",
        has_ecig_tax=True,
        ecig_tax_rate="20% wholesale",
        ecig_tax_structure="wholesale %",
        indoor_vaping_ban=False,
        state_t21_law=True,
        sources=["Tax Foundation 2025"]
    ),

    StateTobaccoPolicy(
        state="Nevada",
        state_abbr="NV",
        flavored_ecig_ban="none",
        flavored_ecig_details="No statewide restrictions on flavored e-cigarettes",
        has_ecig_tax=True,
        ecig_tax_rate="30% wholesale",
        ecig_tax_structure="wholesale %",
        indoor_vaping_ban=False,
        state_t21_law=True,
        sources=["Tax Foundation 2025"]
    ),

    StateTobaccoPolicy(
        state="New Hampshire",
        state_abbr="NH",
        flavored_ecig_ban="none",
        flavored_ecig_details="No statewide restrictions on flavored e-cigarettes",
        has_ecig_tax=True,
        ecig_tax_rate="8% wholesale (open), $0.30/mL (closed)",
        ecig_tax_structure="hybrid",
        indoor_vaping_ban=False,
        state_t21_law=True,
        sources=["Tax Foundation 2025"]
    ),

    StateTobaccoPolicy(
        state="New Jersey",
        state_abbr="NJ",
        flavored_ecig_ban="comprehensive",
        flavored_ecig_details="Comprehensive ban on flavored e-cigarettes (tobacco flavor only allowed). Does NOT ban menthol cigarettes.",
        flavored_ecig_effective_date="2020-04-20",
        menthol_cig_ban=False,
        has_ecig_tax=True,
        ecig_tax_rate="10% retail",
        ecig_tax_structure="retail %",
        indoor_vaping_ban=True,
        indoor_ban_details="Comprehensive smoke-free law covering e-cigarettes",
        state_t21_law=True,
        sources=["Campaign for Tobacco-Free Kids 2024", "Tax Foundation 2025", "VapeRanger 2025"]
    ),

    StateTobaccoPolicy(
        state="New Mexico",
        state_abbr="NM",
        flavored_ecig_ban="none",
        flavored_ecig_details="No statewide restrictions on flavored e-cigarettes",
        has_ecig_tax=True,
        ecig_tax_rate="$0.50 per cartridge",
        ecig_tax_structure="per cartridge",
        indoor_vaping_ban=True,
        indoor_ban_details="Comprehensive smoke-free law covering e-cigarettes",
        state_t21_law=True,
        sources=["Tax Foundation 2025", "Truth Initiative 2025"]
    ),

    StateTobaccoPolicy(
        state="New York",
        state_abbr="NY",
        flavored_ecig_ban="comprehensive",
        flavored_ecig_details="Comprehensive ban on flavored e-cigarettes (tobacco flavor only allowed). Does NOT ban menthol cigarettes.",
        flavored_ecig_effective_date="2020-05-18",
        menthol_cig_ban=False,
        has_ecig_tax=True,
        ecig_tax_rate="20% retail",
        ecig_tax_structure="retail %",
        indoor_vaping_ban=True,
        indoor_ban_details="Comprehensive smoke-free law covering e-cigarettes",
        state_t21_law=True,
        sources=["Campaign for Tobacco-Free Kids 2024", "Tax Foundation 2025", "VapeRanger 2025"]
    ),

    StateTobaccoPolicy(
        state="North Carolina",
        state_abbr="NC",
        flavored_ecig_ban="partial",
        flavored_ecig_details="As of July 1, 2025, only disposable vapes listed on state directory of FDA-authorized products can be sold",
        flavored_ecig_effective_date="2025-07-01",
        has_ecig_tax=True,
        ecig_tax_rate="12.8% wholesale (open), $0.05/mL (closed)",
        ecig_tax_structure="hybrid",
        indoor_vaping_ban=False,
        state_t21_law=True,
        recent_changes="New FDA-authorized product requirement as of July 2025",
        sources=["Tax Foundation 2025", "VapeRanger 2025"]
    ),

    StateTobaccoPolicy(
        state="North Dakota",
        state_abbr="ND",
        flavored_ecig_ban="none",
        flavored_ecig_details="No statewide restrictions on flavored e-cigarettes",
        has_ecig_tax=False,
        indoor_vaping_ban=True,
        indoor_ban_details="Comprehensive smoke-free law covering e-cigarettes",
        state_t21_law=True,
        sources=["Tax Foundation 2025", "Truth Initiative 2025"]
    ),

    StateTobaccoPolicy(
        state="Ohio",
        state_abbr="OH",
        flavored_ecig_ban="partial",
        flavored_ecig_details="Statewide flavor ban enacted in 2025",
        flavored_ecig_effective_date="2025",
        has_ecig_tax=True,
        ecig_tax_rate="10% retail",
        ecig_tax_structure="retail %",
        indoor_vaping_ban=False,
        state_t21_law=True,
        recent_changes="State flavor ban enacted 2025. Court ruled state preemption of local tobacco laws unconstitutional (May 2024).",
        local_restrictions=["Columbus and 13 other municipalities have local flavor restrictions"],
        sources=["Tax Foundation 2025", "VapeRanger 2025", "Campaign for Tobacco-Free Kids 2024"]
    ),

    StateTobaccoPolicy(
        state="Oklahoma",
        state_abbr="OK",
        flavored_ecig_ban="none",
        flavored_ecig_details="No statewide restrictions on flavored e-cigarettes",
        has_ecig_tax=False,
        indoor_vaping_ban=False,
        state_t21_law=True,
        sources=["Tax Foundation 2025"]
    ),

    StateTobaccoPolicy(
        state="Oregon",
        state_abbr="OR",
        flavored_ecig_ban="none",
        flavored_ecig_details="No statewide flavor ban, but many local restrictions",
        has_ecig_tax=True,
        ecig_tax_rate="65% wholesale",
        ecig_tax_structure="wholesale %",
        indoor_vaping_ban=True,
        indoor_ban_details="Comprehensive smoke-free law covering e-cigarettes",
        state_t21_law=True,
        recent_changes="Oregon Court of Appeals upheld Washington County's flavored tobacco law (May 2024)",
        local_restrictions=["Washington County and other localities have flavor restrictions"],
        sources=["Tax Foundation 2025", "Campaign for Tobacco-Free Kids 2024", "Truth Initiative 2025"]
    ),

    StateTobaccoPolicy(
        state="Pennsylvania",
        state_abbr="PA",
        flavored_ecig_ban="none",
        flavored_ecig_details="No statewide restrictions on flavored e-cigarettes",
        has_ecig_tax=True,
        ecig_tax_rate="40% wholesale",
        ecig_tax_structure="wholesale %",
        indoor_vaping_ban=False,
        state_t21_law=True,
        sources=["Tax Foundation 2025"]
    ),

    StateTobaccoPolicy(
        state="Rhode Island",
        state_abbr="RI",
        flavored_ecig_ban="comprehensive",
        flavored_ecig_details="Comprehensive ban on flavored e-cigarettes except tobacco and menthol, enforced Jan 1, 2025 (made permanent from 2019 executive order)",
        flavored_ecig_effective_date="2025-01-01",
        menthol_cig_ban=False,
        has_ecig_tax=True,
        ecig_tax_rate="10% wholesale (open), $0.50/mL (closed)",
        ecig_tax_structure="hybrid",
        indoor_vaping_ban=True,
        indoor_ban_details="Comprehensive smoke-free law covering e-cigarettes",
        state_t21_law=True,
        recent_changes="Flavor ban made permanent as of Jan 1, 2025. New e-cig tax enacted Jan 1, 2025.",
        sources=["Tax Foundation 2025", "VapeRanger 2025", "Campaign for Tobacco-Free Kids 2024"]
    ),

    StateTobaccoPolicy(
        state="South Carolina",
        state_abbr="SC",
        flavored_ecig_ban="none",
        flavored_ecig_details="No statewide restrictions on flavored e-cigarettes",
        has_ecig_tax=False,
        indoor_vaping_ban=False,
        state_t21_law=False,
        sources=["Tax Foundation 2025"]
    ),

    StateTobaccoPolicy(
        state="South Dakota",
        state_abbr="SD",
        flavored_ecig_ban="none",
        flavored_ecig_details="No statewide restrictions on flavored e-cigarettes",
        has_ecig_tax=False,
        indoor_vaping_ban=False,
        state_t21_law=True,
        sources=["Tax Foundation 2025"]
    ),

    StateTobaccoPolicy(
        state="Tennessee",
        state_abbr="TN",
        flavored_ecig_ban="none",
        flavored_ecig_details="No statewide restrictions on flavored e-cigarettes",
        has_ecig_tax=False,
        indoor_vaping_ban=False,
        state_t21_law=True,
        sources=["Tax Foundation 2025"]
    ),

    StateTobaccoPolicy(
        state="Texas",
        state_abbr="TX",
        flavored_ecig_ban="partial",
        flavored_ecig_details="State flavor ban enacted 2025. Additionally, SB 2024 prohibits sale of e-cigarette products made in China and pre-filled with liquid (effective June 2025)",
        flavored_ecig_effective_date="2025",
        has_ecig_tax=False,
        indoor_vaping_ban=False,
        state_t21_law=True,
        recent_changes="Flavor ban and China-made product ban enacted 2025",
        sources=["Tax Foundation 2025", "VapeRanger 2025"]
    ),

    StateTobaccoPolicy(
        state="Utah",
        state_abbr="UT",
        flavored_ecig_ban="comprehensive",
        flavored_ecig_details="Comprehensive ban on flavored vapes except tobacco and menthol (effective Jan 1, 2025, upheld by federal judge March 2025)",
        flavored_ecig_effective_date="2025-01-01",
        menthol_cig_ban=False,
        has_ecig_tax=True,
        ecig_tax_rate="56% manufacturer",
        ecig_tax_structure="manufacturer %",
        indoor_vaping_ban=True,
        indoor_ban_details="Comprehensive smoke-free law covering e-cigarettes",
        state_t21_law=True,
        recent_changes="Flavor ban effective Jan 1, 2025, upheld by federal court March 2025",
        sources=["Tax Foundation 2025", "VapeRanger 2025", "Campaign for Tobacco-Free Kids 2024"]
    ),

    StateTobaccoPolicy(
        state="Vermont",
        state_abbr="VT",
        flavored_ecig_ban="none",
        flavored_ecig_details="No statewide restrictions on flavored e-cigarettes",
        has_ecig_tax=True,
        ecig_tax_rate="92% wholesale",
        ecig_tax_structure="wholesale %",
        indoor_vaping_ban=True,
        indoor_ban_details="Comprehensive smoke-free law covering e-cigarettes",
        state_t21_law=True,
        sources=["Tax Foundation 2025", "Truth Initiative 2025"]
    ),

    StateTobaccoPolicy(
        state="Virginia",
        state_abbr="VA",
        flavored_ecig_ban="none",
        flavored_ecig_details="No statewide restrictions on flavored e-cigarettes",
        has_ecig_tax=True,
        ecig_tax_rate="$0.11 per mL (increased from $0.066 in 2024)",
        ecig_tax_structure="per mL",
        indoor_vaping_ban=False,
        state_t21_law=True,
        recent_changes="E-cig tax increased to $0.11/mL in 2024",
        sources=["Tax Foundation 2025"]
    ),

    StateTobaccoPolicy(
        state="Washington",
        state_abbr="WA",
        flavored_ecig_ban="partial",
        flavored_ecig_details="State flavor ban on e-cigarettes",
        has_ecig_tax=True,
        ecig_tax_rate="27% wholesale (open), $0.09/mL (closed)",
        ecig_tax_structure="hybrid",
        indoor_vaping_ban=True,
        indoor_ban_details="Comprehensive public vaping ban in indoor workplaces, restaurants, and bars",
        state_t21_law=True,
        sources=["Tax Foundation 2025", "VapeRanger 2025"]
    ),

    StateTobaccoPolicy(
        state="West Virginia",
        state_abbr="WV",
        flavored_ecig_ban="none",
        flavored_ecig_details="No statewide restrictions on flavored e-cigarettes",
        has_ecig_tax=True,
        ecig_tax_rate="17.5% manufacturer (open), $0.075/mL (closed)",
        ecig_tax_structure="hybrid",
        indoor_vaping_ban=False,
        state_t21_law=True,
        sources=["Tax Foundation 2025"]
    ),

    StateTobaccoPolicy(
        state="Wisconsin",
        state_abbr="WI",
        flavored_ecig_ban="partial",
        flavored_ecig_details="Similar law to North Carolina requiring FDA-authorized products, set for Sep 1, 2025 (may be subject to legal challenges)",
        flavored_ecig_effective_date="2025-09-01",
        has_ecig_tax=True,
        ecig_tax_rate="5¢ per mL",
        ecig_tax_structure="per mL",
        indoor_vaping_ban=False,
        state_t21_law=True,
        recent_changes="FDA-authorized product requirement scheduled for Sep 2025, facing legal challenges",
        sources=["Tax Foundation 2025", "VapeRanger 2025"]
    ),

    StateTobaccoPolicy(
        state="Wyoming",
        state_abbr="WY",
        flavored_ecig_ban="none",
        flavored_ecig_details="No statewide restrictions on flavored e-cigarettes",
        has_ecig_tax=True,
        ecig_tax_rate="15% wholesale",
        ecig_tax_structure="wholesale %",
        indoor_vaping_ban=False,
        state_t21_law=True,
        sources=["Tax Foundation 2025"]
    ),

    StateTobaccoPolicy(
        state="District of Columbia",
        state_abbr="DC",
        flavored_ecig_ban="comprehensive",
        flavored_ecig_details="Comprehensive flavor restrictions on e-cigarettes",
        has_ecig_tax=True,
        ecig_tax_rate="96% wholesale",
        ecig_tax_structure="wholesale %",
        indoor_vaping_ban=True,
        state_t21_law=True,
        sources=["Tax Foundation 2025", "VapeRanger 2025"]
    ),
]


def export_to_json(filename: str = "state_policies.json"):
    """Export all state data to JSON"""
    data = {
        "metadata": {
            "last_updated": "2024-12-24",
            "data_version": "1.0",
            "sources": [
                "Truth Initiative Flavored Tobacco Restrictions Q2 2025",
                "Campaign for Tobacco-Free Kids State Policy Database 2024",
                "Tax Foundation Vaping Taxes by State 2025",
                "CDC STATE System",
                "FDA Tobacco 21 Resources",
                "State Legislative Sources"
            ],
            "notes": "Federal T21 law applies to all states. Data current as of December 2024/January 2025."
        },
        "states": [state.to_dict() for state in STATES]
    }

    with open(filename, 'w') as f:
        json.dump(data, f, indent=2)

    print(f"Exported {len(STATES)} state policies to {filename}")


def generate_summary_stats():
    """Generate summary statistics"""
    total_states = len(STATES)

    comprehensive_ban = sum(1 for s in STATES if s.flavored_ecig_ban == "comprehensive")
    partial_ban = sum(1 for s in STATES if s.flavored_ecig_ban == "partial")
    no_ban = sum(1 for s in STATES if s.flavored_ecig_ban == "none")

    menthol_bans = sum(1 for s in STATES if s.menthol_cig_ban)

    with_tax = sum(1 for s in STATES if s.has_ecig_tax)
    without_tax = total_states - with_tax

    indoor_bans = sum(1 for s in STATES if s.indoor_vaping_ban)

    print(f"\n{'='*60}")
    print("STATE VAPING & TOBACCO POLICY SUMMARY")
    print(f"{'='*60}\n")

    print(f"Total jurisdictions: {total_states}")
    print()

    print("FLAVORED E-CIGARETTE RESTRICTIONS:")
    print(f"  Comprehensive bans: {comprehensive_ban} states")
    print(f"  Partial restrictions: {partial_ban} states")
    print(f"  No restrictions: {no_ban} states")
    print()

    print("MENTHOL CIGARETTE BANS:")
    print(f"  States with menthol bans: {menthol_bans}")
    print(f"  (Massachusetts, California)")
    print()

    print("E-CIGARETTE EXCISE TAXES:")
    print(f"  States with e-cig tax: {with_tax}")
    print(f"  States without e-cig tax: {without_tax}")
    print()

    print("INDOOR VAPING RESTRICTIONS:")
    print(f"  States with comprehensive indoor vaping bans: {indoor_bans}")
    print()

    print(f"{'='*60}\n")


if __name__ == '__main__':
    generate_summary_stats()
    export_to_json()
