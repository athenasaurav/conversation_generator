# Debt Collection Conversation Scenarios
# This file defines 100 diverse scenarios for debt collection conversations

DEBT_COLLECTION_SCENARIOS = [
    # Basic Payment Scenarios (1-10)
    {
        "id": "basic_payment_willing",
        "name": "Customer willing to pay immediately",
        "description": "Customer acknowledges debt and agrees to pay within timeframe",
        "customer_behavior": "cooperative",
        "outcome": "positive",
        "special_tags": ["function_1"]
    },
    {
        "id": "basic_payment_delayed",
        "name": "Customer needs a few days to pay",
        "description": "Customer acknowledges debt but needs time within the 10-day window",
        "customer_behavior": "cooperative_delayed",
        "outcome": "positive",
        "special_tags": ["function_1"]
    },
    {
        "id": "basic_payment_refused",
        "name": "Customer refuses to pay",
        "description": "Customer acknowledges debt but refuses to pay",
        "customer_behavior": "uncooperative",
        "outcome": "negative",
        "special_tags": ["disconnect"]
    },
    {
        "id": "basic_payment_partial",
        "name": "Customer offers partial payment",
        "description": "Customer wants to pay only part of the debt",
        "customer_behavior": "negotiating",
        "outcome": "negative",
        "special_tags": ["function_2"]
    },
    {
        "id": "basic_payment_confusion",
        "name": "Customer confused about amount",
        "description": "Customer acknowledges debt but disputes the amount",
        "customer_behavior": "confused",
        "outcome": "neutral",
        "special_tags": ["function_1"]
    },
    {
        "id": "basic_payment_already_paid",
        "name": "Customer claims already paid",
        "description": "Customer insists they already paid the debt",
        "customer_behavior": "disputing",
        "outcome": "dispute",
        "special_tags": ["function_2"]
    },
    {
        "id": "basic_payment_financial_hardship",
        "name": "Customer experiencing financial hardship",
        "description": "Customer acknowledges debt but claims financial difficulties",
        "customer_behavior": "hardship",
        "outcome": "negative",
        "special_tags": ["function_1"]
    },
    {
        "id": "basic_payment_medical_emergency",
        "name": "Customer has medical emergency",
        "description": "Customer cannot pay due to medical expenses",
        "customer_behavior": "hardship",
        "outcome": "negative",
        "special_tags": ["function_1"]
    },
    {
        "id": "basic_payment_job_loss",
        "name": "Customer lost their job",
        "description": "Customer recently unemployed and cannot pay",
        "customer_behavior": "hardship",
        "outcome": "negative",
        "special_tags": ["function_1"]
    },
    {
        "id": "basic_payment_family_emergency",
        "name": "Customer has family emergency",
        "description": "Customer dealing with family crisis affecting finances",
        "customer_behavior": "hardship",
        "outcome": "negative",
        "special_tags": ["function_1"]
    },

    # Wrong Person Contacted (11-20)
    {
        "id": "wrong_person_family",
        "name": "Family member answers phone",
        "description": "Spouse, parent, or child answers instead of debtor",
        "customer_behavior": "wrong_person",
        "outcome": "transfer",
        "special_tags": ["transfer"]
    },
    {
        "id": "wrong_person_roommate",
        "name": "Roommate answers phone",
        "description": "Roommate or housemate answers the call",
        "customer_behavior": "wrong_person",
        "outcome": "transfer",
        "special_tags": ["transfer"]
    },
    {
        "id": "wrong_person_coworker",
        "name": "Coworker answers phone",
        "description": "Work colleague answers the phone",
        "customer_behavior": "wrong_person",
        "outcome": "transfer",
        "special_tags": ["transfer"]
    },
    {
        "id": "wrong_person_stranger",
        "name": "Complete stranger answers",
        "description": "Wrong number, person doesn't know the debtor",
        "customer_behavior": "wrong_person",
        "outcome": "disconnect",
        "special_tags": ["disconnect"]
    },
    {
        "id": "wrong_person_business",
        "name": "Business receptionist answers",
        "description": "Called a business number instead of personal",
        "customer_behavior": "wrong_person",
        "outcome": "transfer",
        "special_tags": ["transfer"]
    },
    {
        "id": "wrong_person_ex_spouse",
        "name": "Ex-spouse answers phone",
        "description": "Former spouse answers, may or may not help",
        "customer_behavior": "wrong_person",
        "outcome": "transfer",
        "special_tags": ["transfer"]
    },
    {
        "id": "wrong_person_landlord",
        "name": "Landlord answers phone",
        "description": "Property owner answers, debtor moved out",
        "customer_behavior": "wrong_person",
        "outcome": "disconnect",
        "special_tags": ["disconnect"]
    },
    {
        "id": "wrong_person_new_owner",
        "name": "New phone number owner",
        "description": "Number was reassigned to someone else",
        "customer_behavior": "wrong_person",
        "outcome": "disconnect",
        "special_tags": ["disconnect"]
    },
    {
        "id": "wrong_person_friend",
        "name": "Friend answers phone",
        "description": "Friend of debtor answers the call",
        "customer_behavior": "wrong_person",
        "outcome": "transfer",
        "special_tags": ["transfer"]
    },
    {
        "id": "wrong_person_neighbor",
        "name": "Neighbor answers phone",
        "description": "Neighbor answers, debtor moved away",
        "customer_behavior": "wrong_person",
        "outcome": "disconnect",
        "special_tags": ["disconnect"]
    },

    # Technical Issues (21-30)
    {
        "id": "tech_poor_connection",
        "name": "Poor phone connection",
        "description": "Call has bad audio quality, static, or drops",
        "customer_behavior": "technical",
        "outcome": "disconnect",
        "special_tags": ["disconnect"]
    },
    {
        "id": "tech_call_drops",
        "name": "Call gets disconnected",
        "description": "Call drops in the middle of conversation",
        "customer_behavior": "technical",
        "outcome": "disconnect",
        "special_tags": ["disconnect"]
    },
    {
        "id": "tech_voicemail",
        "name": "Reaches voicemail",
        "description": "Call goes to voicemail system",
        "customer_behavior": "technical",
        "outcome": "disconnect",
        "special_tags": ["disconnect"]
    },
    {
        "id": "tech_busy_signal",
        "name": "Line is busy",
        "description": "Phone line is busy when calling",
        "customer_behavior": "technical",
        "outcome": "disconnect",
        "special_tags": ["disconnect"]
    },
    {
        "id": "tech_no_answer",
        "name": "No one answers",
        "description": "Phone rings but no one picks up",
        "customer_behavior": "technical",
        "outcome": "disconnect",
        "special_tags": ["disconnect"]
    },
    {
        "id": "tech_number_disconnected",
        "name": "Number is disconnected",
        "description": "Phone number is no longer in service",
        "customer_behavior": "technical",
        "outcome": "disconnect",
        "special_tags": ["disconnect"]
    },
    {
        "id": "tech_hearing_impaired",
        "name": "Customer is hearing impaired",
        "description": "Customer has difficulty hearing the agent",
        "customer_behavior": "technical",
        "outcome": "transfer",
        "special_tags": ["transfer"]
    },
    {
        "id": "tech_language_barrier",
        "name": "Language barrier",
        "description": "Customer doesn't speak the agent's language well",
        "customer_behavior": "technical",
        "outcome": "transfer",
        "special_tags": ["transfer"]
    },
    {
        "id": "tech_echo_feedback",
        "name": "Echo or feedback on line",
        "description": "Technical audio issues making conversation difficult",
        "customer_behavior": "technical",
        "outcome": "disconnect",
        "special_tags": ["disconnect"]
    },
    {
        "id": "tech_automated_system",
        "name": "Reaches automated system",
        "description": "Call connects to automated phone system",
        "customer_behavior": "technical",
        "outcome": "disconnect",
        "special_tags": ["disconnect"]
    },

    # Hostile/Aggressive Customers (31-40)
    {
        "id": "hostile_angry_yelling",
        "name": "Customer is angry and yelling",
        "description": "Customer becomes very aggressive and hostile",
        "customer_behavior": "hostile",
        "outcome": "negative",
        "special_tags": ["disconnect"]
    },
    {
        "id": "hostile_threatening",
        "name": "Customer makes threats",
        "description": "Customer threatens the agent or company",
        "customer_behavior": "hostile",
        "outcome": "negative",
        "special_tags": ["disconnect"]
    },
    {
        "id": "hostile_profanity",
        "name": "Customer uses profanity",
        "description": "Customer swears and uses inappropriate language",
        "customer_behavior": "hostile",
        "outcome": "negative",
        "special_tags": ["disconnect"]
    },
    {
        "id": "hostile_harassment_claims",
        "name": "Customer claims harassment",
        "description": "Customer accuses agent of harassment",
        "customer_behavior": "hostile",
        "outcome": "negative",
        "special_tags": ["function_2"]
    },
    {
        "id": "hostile_legal_threats",
        "name": "Customer threatens legal action",
        "description": "Customer threatens to sue the company",
        "customer_behavior": "hostile",
        "outcome": "negative",
        "special_tags": ["function_2"]
    },
    {
        "id": "hostile_recording_threat",
        "name": "Customer threatens to record",
        "description": "Customer says they're recording the call",
        "customer_behavior": "hostile",
        "outcome": "neutral",
        "special_tags": ["function_2"]
    },
    {
        "id": "hostile_complaint_threat",
        "name": "Customer threatens to file complaint",
        "description": "Customer threatens regulatory complaint",
        "customer_behavior": "hostile",
        "outcome": "negative",
        "special_tags": ["function_2"]
    },
    {
        "id": "hostile_media_threat",
        "name": "Customer threatens media exposure",
        "description": "Customer threatens to go to media/social media",
        "customer_behavior": "hostile",
        "outcome": "negative",
        "special_tags": ["function_2"]
    },
    {
        "id": "hostile_personal_attacks",
        "name": "Customer makes personal attacks",
        "description": "Customer attacks agent personally",
        "customer_behavior": "hostile",
        "outcome": "negative",
        "special_tags": ["disconnect"]
    },
    {
        "id": "hostile_hangs_up_angry",
        "name": "Customer hangs up angrily",
        "description": "Customer ends call abruptly in anger",
        "customer_behavior": "hostile",
        "outcome": "negative",
        "special_tags": ["disconnect"]
    },

    # Legal/Regulatory Issues (41-50)
    {
        "id": "legal_bankruptcy",
        "name": "Customer filed for bankruptcy",
        "description": "Customer is in bankruptcy proceedings",
        "customer_behavior": "legal",
        "outcome": "legal",
        "special_tags": ["function_2"]
    },
    {
        "id": "legal_attorney_representation",
        "name": "Customer has attorney",
        "description": "Customer is represented by legal counsel",
        "customer_behavior": "legal",
        "outcome": "legal",
        "special_tags": ["transfer"]
    },
    {
        "id": "legal_cease_desist",
        "name": "Customer demands cease and desist",
        "description": "Customer formally requests no more contact",
        "customer_behavior": "legal",
        "outcome": "legal",
        "special_tags": ["function_2"]
    },
    {
        "id": "legal_dispute_debt",
        "name": "Customer formally disputes debt",
        "description": "Customer legally disputes the debt validity",
        "customer_behavior": "legal",
        "outcome": "legal",
        "special_tags": ["function_2"]
    },
    {
        "id": "legal_identity_theft",
        "name": "Customer claims identity theft",
        "description": "Customer says debt is from identity theft",
        "customer_behavior": "legal",
        "outcome": "legal",
        "special_tags": ["function_2"]
    },
    {
        "id": "legal_deceased_debtor",
        "name": "Debtor is deceased",
        "description": "Family member reports debtor has died",
        "customer_behavior": "legal",
        "outcome": "legal",
        "special_tags": ["function_2"]
    },
    {
        "id": "legal_military_deployment",
        "name": "Customer is deployed military",
        "description": "Customer is on military deployment",
        "customer_behavior": "legal",
        "outcome": "legal",
        "special_tags": ["function_2"]
    },
    {
        "id": "legal_statute_limitations",
        "name": "Customer claims statute of limitations",
        "description": "Customer says debt is too old to collect",
        "customer_behavior": "legal",
        "outcome": "legal",
        "special_tags": ["function_2"]
    },
    {
        "id": "legal_fraud_claim",
        "name": "Customer claims fraud",
        "description": "Customer says the debt is fraudulent",
        "customer_behavior": "legal",
        "outcome": "legal",
        "special_tags": ["function_2"]
    },
    {
        "id": "legal_court_order",
        "name": "Customer has court order",
        "description": "Customer has court order regarding debt",
        "customer_behavior": "legal",
        "outcome": "legal",
        "special_tags": ["function_2"]
    },

    # Special Circumstances (51-60)
    {
        "id": "special_elderly_confusion",
        "name": "Elderly customer is confused",
        "description": "Elderly person doesn't understand the situation",
        "customer_behavior": "vulnerable",
        "outcome": "transfer",
        "special_tags": ["transfer"]
    },
    {
        "id": "special_mental_health",
        "name": "Customer has mental health issues",
        "description": "Customer appears to have mental health challenges",
        "customer_behavior": "vulnerable",
        "outcome": "transfer",
        "special_tags": ["transfer"]
    },
    {
        "id": "special_disability",
        "name": "Customer has disability",
        "description": "Customer has physical or cognitive disability",
        "customer_behavior": "vulnerable",
        "outcome": "transfer",
        "special_tags": ["transfer"]
    },
    {
        "id": "special_non_english",
        "name": "Customer doesn't speak English",
        "description": "Customer needs interpreter services",
        "customer_behavior": "language",
        "outcome": "transfer",
        "special_tags": ["transfer"]
    },
    {
        "id": "special_minor_child",
        "name": "Minor child answers phone",
        "description": "Child under 18 answers the call",
        "customer_behavior": "minor",
        "outcome": "disconnect",
        "special_tags": ["disconnect"]
    },
    {
        "id": "special_hospitalized",
        "name": "Customer is hospitalized",
        "description": "Customer is currently in hospital",
        "customer_behavior": "medical",
        "outcome": "neutral",
        "special_tags": ["function_1"]
    },
    {
        "id": "special_incarcerated",
        "name": "Customer is in jail/prison",
        "description": "Customer is currently incarcerated",
        "customer_behavior": "incarcerated",
        "outcome": "neutral",
        "special_tags": ["function_2"]
    },
    {
        "id": "special_natural_disaster",
        "name": "Customer affected by natural disaster",
        "description": "Customer's area hit by hurricane, flood, etc.",
        "customer_behavior": "disaster",
        "outcome": "neutral",
        "special_tags": ["function_1"]
    },
    {
        "id": "special_covid_impact",
        "name": "Customer affected by pandemic",
        "description": "Customer lost job/income due to COVID-19",
        "customer_behavior": "pandemic",
        "outcome": "negative",
        "special_tags": ["function_1"]
    },
    {
        "id": "special_military_active",
        "name": "Active military service member",
        "description": "Customer is active duty military",
        "customer_behavior": "military",
        "outcome": "legal",
        "special_tags": ["function_2"]
    },

    # Business/Employment Related (61-70)
    {
        "id": "business_workplace_call",
        "name": "Called customer at workplace",
        "description": "Agent reaches customer at their job",
        "customer_behavior": "workplace",
        "outcome": "neutral",
        "special_tags": ["function_1"]
    },
    {
        "id": "business_employer_contact",
        "name": "Employer answers phone",
        "description": "Customer's boss or HR answers",
        "customer_behavior": "employer",
        "outcome": "transfer",
        "special_tags": ["transfer"]
    },
    {
        "id": "business_self_employed",
        "name": "Customer is self-employed",
        "description": "Customer runs their own business",
        "customer_behavior": "business_owner",
        "outcome": "neutral",
        "special_tags": ["function_1"]
    },
    {
        "id": "business_seasonal_worker",
        "name": "Customer is seasonal worker",
        "description": "Customer only works certain times of year",
        "customer_behavior": "seasonal",
        "outcome": "negative",
        "special_tags": ["function_1"]
    },
    {
        "id": "business_commission_based",
        "name": "Customer works on commission",
        "description": "Customer's income varies by performance",
        "customer_behavior": "variable_income",
        "outcome": "negative",
        "special_tags": ["function_1"]
    },
    {
        "id": "business_recently_fired",
        "name": "Customer was recently fired",
        "description": "Customer lost job recently",
        "customer_behavior": "unemployed",
        "outcome": "negative",
        "special_tags": ["function_1"]
    },
    {
        "id": "business_retirement",
        "name": "Customer is retired",
        "description": "Customer is on fixed retirement income",
        "customer_behavior": "retired",
        "outcome": "negative",
        "special_tags": ["function_1"]
    },
    {
        "id": "business_student",
        "name": "Customer is a student",
        "description": "Customer is in school with limited income",
        "customer_behavior": "student",
        "outcome": "negative",
        "special_tags": ["function_1"]
    },
    {
        "id": "business_gig_worker",
        "name": "Customer is gig worker",
        "description": "Customer drives for Uber, delivers food, etc.",
        "customer_behavior": "gig_economy",
        "outcome": "negative",
        "special_tags": ["function_1"]
    },
    {
        "id": "business_new_job",
        "name": "Customer just started new job",
        "description": "Customer recently got employment",
        "customer_behavior": "new_employment",
        "outcome": "positive",
        "special_tags": ["function_1"]
    },

    # Payment Method Issues (71-80)
    {
        "id": "payment_no_bank_account",
        "name": "Customer has no bank account",
        "description": "Customer is unbanked",
        "customer_behavior": "unbanked",
        "outcome": "neutral",
        "special_tags": ["function_1"]
    },
    {
        "id": "payment_frozen_account",
        "name": "Customer's account is frozen",
        "description": "Bank account is frozen or closed",
        "customer_behavior": "account_issues",
        "outcome": "negative",
        "special_tags": ["function_1"]
    },
    {
        "id": "payment_card_declined",
        "name": "Customer's card was declined",
        "description": "Payment method doesn't work",
        "customer_behavior": "payment_failure",
        "outcome": "negative",
        "special_tags": ["function_1"]
    },
    {
        "id": "payment_cash_only",
        "name": "Customer only has cash",
        "description": "Customer wants to pay with cash",
        "customer_behavior": "cash_preference",
        "outcome": "neutral",
        "special_tags": ["function_1"]
    },
    {
        "id": "payment_app_issues",
        "name": "Customer can't use payment app",
        "description": "Technical issues with CashNow app",
        "customer_behavior": "tech_issues",
        "outcome": "neutral",
        "special_tags": ["function_1"]
    },
    {
        "id": "payment_insufficient_funds",
        "name": "Customer has insufficient funds",
        "description": "Not enough money in account",
        "customer_behavior": "insufficient_funds",
        "outcome": "negative",
        "special_tags": ["function_1"]
    },
    {
        "id": "payment_waiting_paycheck",
        "name": "Customer waiting for paycheck",
        "description": "Customer gets paid soon",
        "customer_behavior": "pending_income",
        "outcome": "positive",
        "special_tags": ["function_1"]
    },
    {
        "id": "payment_money_order",
        "name": "Customer wants to pay by money order",
        "description": "Customer prefers money order payment",
        "customer_behavior": "alternative_payment",
        "outcome": "neutral",
        "special_tags": ["function_1"]
    },
    {
        "id": "payment_wire_transfer",
        "name": "Customer offers wire transfer",
        "description": "Customer wants to wire the money",
        "customer_behavior": "alternative_payment",
        "outcome": "neutral",
        "special_tags": ["function_1"]
    },
    {
        "id": "payment_cryptocurrency",
        "name": "Customer offers cryptocurrency",
        "description": "Customer wants to pay with Bitcoin, etc.",
        "customer_behavior": "alternative_payment",
        "outcome": "negative",
        "special_tags": ["function_1"]
    },

    # Family/Personal Situations (81-90)
    {
        "id": "family_divorce",
        "name": "Customer going through divorce",
        "description": "Customer in divorce proceedings",
        "customer_behavior": "personal_crisis",
        "outcome": "negative",
        "special_tags": ["function_1"]
    },
    {
        "id": "family_death",
        "name": "Customer had death in family",
        "description": "Customer dealing with family death",
        "customer_behavior": "grieving",
        "outcome": "negative",
        "special_tags": ["function_1"]
    },
    {
        "id": "family_new_baby",
        "name": "Customer has new baby",
        "description": "Customer has new child, medical expenses",
        "customer_behavior": "new_parent",
        "outcome": "negative",
        "special_tags": ["function_1"]
    },
    {
        "id": "family_caring_elderly",
        "name": "Customer caring for elderly parent",
        "description": "Customer has elderly care expenses",
        "customer_behavior": "caregiver",
        "outcome": "negative",
        "special_tags": ["function_1"]
    },
    {
        "id": "family_child_support",
        "name": "Customer paying child support",
        "description": "Customer has child support obligations",
        "customer_behavior": "child_support",
        "outcome": "negative",
        "special_tags": ["function_1"]
    },
    {
        "id": "family_domestic_violence",
        "name": "Customer is domestic violence victim",
        "description": "Customer in abusive relationship",
        "customer_behavior": "vulnerable",
        "outcome": "transfer",
        "special_tags": ["transfer"]
    },
    {
        "id": "family_addiction_issues",
        "name": "Customer has addiction problems",
        "description": "Customer struggling with substance abuse",
        "customer_behavior": "addiction",
        "outcome": "transfer",
        "special_tags": ["transfer"]
    },
    {
        "id": "family_housing_crisis",
        "name": "Customer facing eviction",
        "description": "Customer about to lose housing",
        "customer_behavior": "housing_crisis",
        "outcome": "negative",
        "special_tags": ["function_1"]
    },
    {
        "id": "family_immigration_issues",
        "name": "Customer has immigration problems",
        "description": "Customer dealing with immigration status",
        "customer_behavior": "immigration",
        "outcome": "negative",
        "special_tags": ["function_1"]
    },
    {
        "id": "family_multiple_debts",
        "name": "Customer has multiple debts",
        "description": "Customer overwhelmed with many debts",
        "customer_behavior": "debt_overwhelmed",
        "outcome": "negative",
        "special_tags": ["function_1"]
    },

    # Miscellaneous Edge Cases (91-100)
    {
        "id": "misc_wrong_debt_amount",
        "name": "Agent has wrong debt amount",
        "description": "System shows incorrect debt amount",
        "customer_behavior": "system_error",
        "outcome": "neutral",
        "special_tags": ["function_2"]
    },
    {
        "id": "misc_duplicate_call",
        "name": "Customer already spoke to agent today",
        "description": "Customer received multiple calls same day",
        "customer_behavior": "duplicate_contact",
        "outcome": "neutral",
        "special_tags": ["function_2"]
    },
    {
        "id": "misc_wrong_customer_name",
        "name": "Agent has wrong customer name",
        "description": "System has incorrect customer information",
        "customer_behavior": "system_error",
        "outcome": "neutral",
        "special_tags": ["function_2"]
    },
    {
        "id": "misc_customer_moved",
        "name": "Customer moved to different country",
        "description": "Customer relocated internationally",
        "customer_behavior": "relocated",
        "outcome": "negative",
        "special_tags": ["function_2"]
    },
    {
        "id": "misc_customer_very_polite",
        "name": "Extremely polite customer",
        "description": "Customer is overly courteous and apologetic",
        "customer_behavior": "overly_polite",
        "outcome": "positive",
        "special_tags": ["function_1"]
    },
    {
        "id": "misc_customer_suspicious",
        "name": "Customer acts suspiciously",
        "description": "Customer behavior seems unusual or evasive",
        "customer_behavior": "suspicious",
        "outcome": "negative",
        "special_tags": ["function_2"]
    },
    {
        "id": "misc_customer_drunk",
        "name": "Customer appears intoxicated",
        "description": "Customer seems under the influence",
        "customer_behavior": "intoxicated",
        "outcome": "disconnect",
        "special_tags": ["disconnect"]
    },
    {
        "id": "misc_background_noise",
        "name": "Loud background noise",
        "description": "Customer in noisy environment",
        "customer_behavior": "environmental",
        "outcome": "neutral",
        "special_tags": ["function_1"]
    },
    {
        "id": "misc_customer_multitasking",
        "name": "Customer is multitasking",
        "description": "Customer distracted, doing other things",
        "customer_behavior": "distracted",
        "outcome": "neutral",
        "special_tags": ["function_1"]
    },
    {
        "id": "misc_perfect_resolution",
        "name": "Perfect customer interaction",
        "description": "Customer is ideal - polite, pays immediately",
        "customer_behavior": "ideal",
        "outcome": "positive",
        "special_tags": ["function_1"]
    }
]

# Special tags that should appear in conversations
SPECIAL_TAGS = [
    "(disconnect)",
    "(transfer)", 
    "(function_1)",
    "(function_2)",
    "(hold)",
    "(mute)",
    "(conference)",
    "(callback)",
    "(escalate)"
]

# Customer behavior types for variation generation
CUSTOMER_BEHAVIORS = {
    "cooperative": "Customer is willing to work with agent",
    "uncooperative": "Customer refuses to cooperate",
    "hostile": "Customer is aggressive or angry",
    "confused": "Customer doesn't understand situation",
    "vulnerable": "Customer needs special handling",
    "legal": "Customer raises legal issues",
    "technical": "Technical issues affect call",
    "wrong_person": "Wrong person contacted"
}

# Outcome types
OUTCOME_TYPES = {
    "positive": "Customer agrees to pay",
    "negative": "Customer refuses to pay", 
    "neutral": "Situation needs follow-up",
    "legal": "Legal issues require escalation",
    "transfer": "Call needs to be transferred",
    "disconnect": "Call ends without resolution",
    "dispute": "Customer disputes the debt"
}

