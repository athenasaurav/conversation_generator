# Debt Collection Conversation Scenarios
# This file defines 130 comprehensive scenarios for debt collection conversations
# Includes all critical real-world scenarios including broken promises and data confirmation

DEBT_COLLECTION_SCENARIOS = [
    # Basic Payment Scenarios (1-10)
    {
        "id": "basic_payment_willing",
        "name": "Customer willing to pay immediately",
        "description": "Customer acknowledges debt and agrees to pay within timeframe",
        "customer_behavior": "cooperative",
        "outcome": "positive",
        "special_tags": ["(function_1)"]
    },
    {
        "id": "basic_payment_delayed",
        "name": "Customer needs a few days to pay",
        "description": "Customer acknowledges debt but needs time within the 10-day window",
        "customer_behavior": "cooperative_delayed",
        "outcome": "positive",
        "special_tags": ["(function_1)"]
    },
    {
        "id": "basic_payment_refused",
        "name": "Customer refuses to pay",
        "description": "Customer acknowledges debt but refuses to pay",
        "customer_behavior": "uncooperative",
        "outcome": "negative",
        "special_tags": ["(disconnect)"]
    },
    {
        "id": "basic_payment_partial",
        "name": "Customer offers partial payment",
        "description": "Customer wants to pay only part of the debt",
        "customer_behavior": "negotiating",
        "outcome": "negative",
        "special_tags": ["(function_2)"]
    },
    {
        "id": "basic_payment_confusion",
        "name": "Customer confused about amount",
        "description": "Customer acknowledges debt but disputes the amount",
        "customer_behavior": "confused",
        "outcome": "neutral",
        "special_tags": ["(function_1)"]
    },
    {
        "id": "basic_payment_already_paid",
        "name": "Customer claims already paid",
        "description": "Customer insists they already paid the debt",
        "customer_behavior": "disputing",
        "outcome": "dispute",
        "special_tags": ["(function_2)"]
    },
    {
        "id": "basic_payment_financial_hardship",
        "name": "Customer experiencing financial hardship",
        "description": "Customer acknowledges debt but claims financial difficulties",
        "customer_behavior": "hardship",
        "outcome": "negative",
        "special_tags": ["(function_1)"]
    },
    {
        "id": "basic_payment_medical_emergency",
        "name": "Customer has medical emergency",
        "description": "Customer cannot pay due to medical expenses",
        "customer_behavior": "hardship",
        "outcome": "negative",
        "special_tags": ["(function_1)"]
    },
    {
        "id": "basic_payment_job_loss",
        "name": "Customer lost their job",
        "description": "Customer recently unemployed and cannot pay",
        "customer_behavior": "hardship",
        "outcome": "negative",
        "special_tags": ["(function_1)"]
    },
    {
        "id": "basic_payment_family_emergency",
        "name": "Customer has family emergency",
        "description": "Customer dealing with family crisis affecting finances",
        "customer_behavior": "hardship",
        "outcome": "negative",
        "special_tags": ["(function_1)"]
    },

    # Wrong Person Contacted (11-20)
    {
        "id": "wrong_person_family",
        "name": "Family member answers phone",
        "description": "Spouse, parent, or child answers instead of debtor",
        "customer_behavior": "wrong_person",
        "outcome": "transfer",
        "special_tags": ["(transfer)"]
    },
    {
        "id": "wrong_person_roommate",
        "name": "Roommate answers phone",
        "description": "Roommate or housemate answers the call",
        "customer_behavior": "wrong_person",
        "outcome": "transfer",
        "special_tags": ["(transfer)"]
    },
    {
        "id": "wrong_person_coworker",
        "name": "Coworker answers phone",
        "description": "Work colleague answers the phone",
        "customer_behavior": "wrong_person",
        "outcome": "transfer",
        "special_tags": ["(transfer)"]
    },
    {
        "id": "wrong_person_neighbor",
        "name": "Neighbor answers phone",
        "description": "Neighbor or friend answers the phone",
        "customer_behavior": "wrong_person",
        "outcome": "transfer",
        "special_tags": ["(transfer)"]
    },
    {
        "id": "wrong_person_business",
        "name": "Business receptionist answers",
        "description": "Business employee answers work phone",
        "customer_behavior": "wrong_person",
        "outcome": "transfer",
        "special_tags": ["(transfer)"]
    },
    {
        "id": "wrong_person_previous_owner",
        "name": "Previous phone number owner",
        "description": "Person who got recycled phone number",
        "customer_behavior": "wrong_person",
        "outcome": "disconnect",
        "special_tags": ["(disconnect)"]
    },
    {
        "id": "wrong_person_minor",
        "name": "Minor child answers phone",
        "description": "Underage child answers the phone",
        "customer_behavior": "wrong_person",
        "outcome": "disconnect",
        "special_tags": ["(disconnect)"]
    },
    {
        "id": "wrong_person_elderly_relative",
        "name": "Elderly relative answers",
        "description": "Elderly parent or grandparent answers",
        "customer_behavior": "wrong_person",
        "outcome": "transfer",
        "special_tags": ["(transfer)"]
    },
    {
        "id": "wrong_person_caregiver",
        "name": "Caregiver answers phone",
        "description": "Professional or family caregiver answers",
        "customer_behavior": "wrong_person",
        "outcome": "transfer",
        "special_tags": ["(transfer)"]
    },
    {
        "id": "wrong_person_refuses_info",
        "name": "Wrong person refuses to help",
        "description": "Person answers but refuses to provide any information",
        "customer_behavior": "wrong_person",
        "outcome": "disconnect",
        "special_tags": ["(disconnect)"]
    },

    # Hostile Customer Scenarios (21-30)
    {
        "id": "hostile_customer_angry",
        "name": "Customer is very angry",
        "description": "Customer is shouting and using aggressive language",
        "customer_behavior": "hostile",
        "outcome": "negative",
        "special_tags": ["(disconnect)"]
    },
    {
        "id": "hostile_customer_abusive",
        "name": "Customer using abusive language",
        "description": "Customer using profanity and personal attacks",
        "customer_behavior": "hostile",
        "outcome": "negative",
        "special_tags": ["(disconnect)"]
    },
    {
        "id": "hostile_customer_threatening",
        "name": "Customer making threats",
        "description": "Customer threatening legal action or violence",
        "customer_behavior": "hostile",
        "outcome": "negative",
        "special_tags": ["(disconnect)"]
    },
    {
        "id": "hostile_customer_harassment_claim",
        "name": "Customer claims harassment",
        "description": "Customer accuses agent of harassment",
        "customer_behavior": "hostile",
        "outcome": "negative",
        "special_tags": ["(transfer)"]
    },
    {
        "id": "hostile_customer_recording",
        "name": "Customer recording the call",
        "description": "Customer announces they are recording for legal purposes",
        "customer_behavior": "hostile",
        "outcome": "neutral",
        "special_tags": ["(function_1)"]
    },
    {
        "id": "hostile_customer_lawyer_threat",
        "name": "Customer threatens lawyer involvement",
        "description": "Customer threatens to involve attorney",
        "customer_behavior": "hostile",
        "outcome": "negative",
        "special_tags": ["(transfer)"]
    },
    {
        "id": "hostile_customer_complaint_threat",
        "name": "Customer threatens to file complaint",
        "description": "Customer threatens regulatory complaint",
        "customer_behavior": "hostile",
        "outcome": "negative",
        "special_tags": ["(transfer)"]
    },
    {
        "id": "hostile_customer_media_threat",
        "name": "Customer threatens media exposure",
        "description": "Customer threatens to go to news/social media",
        "customer_behavior": "hostile",
        "outcome": "negative",
        "special_tags": ["(transfer)"]
    },
    {
        "id": "hostile_customer_hangs_up_repeatedly",
        "name": "Customer keeps hanging up",
        "description": "Customer hangs up immediately when called",
        "customer_behavior": "hostile",
        "outcome": "negative",
        "special_tags": ["(disconnect)"]
    },
    {
        "id": "hostile_customer_demands_supervisor",
        "name": "Customer demands supervisor immediately",
        "description": "Customer refuses to speak with agent, wants manager",
        "customer_behavior": "hostile",
        "outcome": "transfer",
        "special_tags": ["(transfer)"]
    },

    # Legal/Dispute Scenarios (31-40)
    {
        "id": "legal_dispute_debt_validity",
        "name": "Customer disputes debt validity",
        "description": "Customer claims debt is not theirs or invalid",
        "customer_behavior": "disputing",
        "outcome": "dispute",
        "special_tags": ["(transfer)"]
    },
    {
        "id": "legal_dispute_amount",
        "name": "Customer disputes amount owed",
        "description": "Customer agrees debt exists but disputes amount",
        "customer_behavior": "disputing",
        "outcome": "dispute",
        "special_tags": ["(transfer)"]
    },
    {
        "id": "legal_cease_and_desist",
        "name": "Customer requests cease and desist",
        "description": "Customer formally requests no more contact",
        "customer_behavior": "legal",
        "outcome": "legal",
        "special_tags": ["(transfer)"]
    },
    {
        "id": "legal_attorney_representation",
        "name": "Customer has attorney representation",
        "description": "Customer is represented by lawyer",
        "customer_behavior": "legal",
        "outcome": "legal",
        "special_tags": ["(transfer)"]
    },
    {
        "id": "legal_bankruptcy_filed",
        "name": "Customer filed for bankruptcy",
        "description": "Customer is in active bankruptcy proceedings",
        "customer_behavior": "legal",
        "outcome": "legal",
        "special_tags": ["(transfer)"]
    },
    {
        "id": "legal_statute_limitations",
        "name": "Customer claims statute of limitations",
        "description": "Customer believes debt is too old to collect",
        "customer_behavior": "legal",
        "outcome": "dispute",
        "special_tags": ["(transfer)"]
    },
    {
        "id": "legal_identity_theft_claim",
        "name": "Customer claims identity theft",
        "description": "Customer claims debt resulted from identity theft",
        "customer_behavior": "disputing",
        "outcome": "dispute",
        "special_tags": ["(transfer)"]
    },
    {
        "id": "legal_fraud_claim",
        "name": "Customer claims fraud",
        "description": "Customer claims fraudulent charges or services",
        "customer_behavior": "disputing",
        "outcome": "dispute",
        "special_tags": ["(transfer)"]
    },
    {
        "id": "legal_deceased_debtor",
        "name": "Debtor is deceased",
        "description": "Family member reports debtor has died",
        "customer_behavior": "legal",
        "outcome": "legal",
        "special_tags": ["(transfer)"]
    },
    {
        "id": "legal_military_protection",
        "name": "Customer claims military protection",
        "description": "Active duty military claiming SCRA protection",
        "customer_behavior": "legal",
        "outcome": "legal",
        "special_tags": ["(transfer)"]
    },

    # Technical Issues (41-50)
    {
        "id": "technical_poor_connection",
        "name": "Poor phone connection",
        "description": "Call quality is poor, difficult to hear",
        "customer_behavior": "technical",
        "outcome": "neutral",
        "special_tags": ["(callback)"]
    },
    {
        "id": "technical_call_drops",
        "name": "Call keeps dropping",
        "description": "Connection keeps getting lost",
        "customer_behavior": "technical",
        "outcome": "neutral",
        "special_tags": ["(callback)"]
    },
    {
        "id": "technical_customer_on_speaker",
        "name": "Customer on speakerphone",
        "description": "Customer using speakerphone, others can hear",
        "customer_behavior": "technical",
        "outcome": "neutral",
        "special_tags": ["(function_1)"]
    },
    {
        "id": "technical_background_noise",
        "name": "Loud background noise",
        "description": "Customer in noisy environment",
        "customer_behavior": "environmental",
        "outcome": "neutral",
        "special_tags": ["(function_1)"]
    },
    {
        "id": "technical_customer_driving",
        "name": "Customer is driving",
        "description": "Customer driving and distracted",
        "customer_behavior": "distracted",
        "outcome": "neutral",
        "special_tags": ["(callback)"]
    },
    {
        "id": "technical_customer_multitasking",
        "name": "Customer is multitasking",
        "description": "Customer distracted, doing other things",
        "customer_behavior": "distracted",
        "outcome": "neutral",
        "special_tags": ["(function_1)"]
    },
    {
        "id": "technical_voicemail_full",
        "name": "Customer's voicemail is full",
        "description": "Cannot leave voicemail, mailbox full",
        "customer_behavior": "technical",
        "outcome": "neutral",
        "special_tags": ["(callback)"]
    },
    {
        "id": "technical_wrong_number_recorded",
        "name": "Wrong number in system",
        "description": "Phone number in system is incorrect",
        "customer_behavior": "technical",
        "outcome": "neutral",
        "special_tags": ["(transfer)"]
    },
    {
        "id": "technical_customer_hearing_impaired",
        "name": "Customer has hearing difficulties",
        "description": "Customer needs accommodation for hearing",
        "customer_behavior": "vulnerable",
        "outcome": "neutral",
        "special_tags": ["(transfer)"]
    },
    {
        "id": "technical_language_barrier",
        "name": "Customer language barrier",
        "description": "Customer doesn't speak language well",
        "customer_behavior": "confused",
        "outcome": "neutral",
        "special_tags": ["(transfer)"]
    },

    # Customer Circumstances (51-60)
    {
        "id": "circumstances_elderly_confused",
        "name": "Elderly customer confused",
        "description": "Elderly customer seems confused about situation",
        "customer_behavior": "vulnerable",
        "outcome": "neutral",
        "special_tags": ["(transfer)"]
    },
    {
        "id": "circumstances_customer_sick",
        "name": "Customer is ill",
        "description": "Customer is currently sick or hospitalized",
        "customer_behavior": "vulnerable",
        "outcome": "neutral",
        "special_tags": ["(callback)"]
    },
    {
        "id": "circumstances_customer_traveling",
        "name": "Customer is traveling",
        "description": "Customer is out of town or country",
        "customer_behavior": "unavailable",
        "outcome": "neutral",
        "special_tags": ["(callback)"]
    },
    {
        "id": "circumstances_customer_at_work",
        "name": "Customer at work",
        "description": "Customer cannot talk privately at work",
        "customer_behavior": "unavailable",
        "outcome": "neutral",
        "special_tags": ["(callback)"]
    },
    {
        "id": "circumstances_customer_with_children",
        "name": "Customer with young children",
        "description": "Customer distracted by children",
        "customer_behavior": "distracted",
        "outcome": "neutral",
        "special_tags": ["(callback)"]
    },
    {
        "id": "circumstances_customer_in_meeting",
        "name": "Customer in meeting",
        "description": "Customer in business meeting or appointment",
        "customer_behavior": "unavailable",
        "outcome": "neutral",
        "special_tags": ["(callback)"]
    },
    {
        "id": "circumstances_customer_grieving",
        "name": "Customer dealing with death in family",
        "description": "Customer recently lost family member",
        "customer_behavior": "vulnerable",
        "outcome": "neutral",
        "special_tags": ["(callback)"]
    },
    {
        "id": "circumstances_customer_divorced",
        "name": "Customer going through divorce",
        "description": "Customer in middle of divorce proceedings",
        "customer_behavior": "distressed",
        "outcome": "neutral",
        "special_tags": ["(function_1)"]
    },
    {
        "id": "circumstances_customer_new_baby",
        "name": "Customer with new baby",
        "description": "Customer recently had baby, financial strain",
        "customer_behavior": "distressed",
        "outcome": "neutral",
        "special_tags": ["(function_1)"]
    },
    {
        "id": "circumstances_customer_moved",
        "name": "Customer recently moved",
        "description": "Customer relocated, address/phone changed",
        "customer_behavior": "cooperative",
        "outcome": "positive",
        "special_tags": ["(function_1)"]
    },

    # Agent Challenges (61-70)
    {
        "id": "agent_challenge_customer_interrupts",
        "name": "Customer constantly interrupts",
        "description": "Customer won't let agent speak",
        "customer_behavior": "hostile",
        "outcome": "negative",
        "special_tags": ["(function_1)"]
    },
    {
        "id": "agent_challenge_customer_silent",
        "name": "Customer remains silent",
        "description": "Customer answers but won't speak",
        "customer_behavior": "uncooperative",
        "outcome": "negative",
        "special_tags": ["(disconnect)"]
    },
    {
        "id": "agent_challenge_customer_lies",
        "name": "Customer telling obvious lies",
        "description": "Customer providing false information",
        "customer_behavior": "uncooperative",
        "outcome": "negative",
        "special_tags": ["(function_1)"]
    },
    {
        "id": "agent_challenge_customer_stalling",
        "name": "Customer stalling for time",
        "description": "Customer deliberately wasting time",
        "customer_behavior": "uncooperative",
        "outcome": "negative",
        "special_tags": ["(function_1)"]
    },
    {
        "id": "agent_challenge_customer_testing",
        "name": "Customer testing agent knowledge",
        "description": "Customer asking complex legal questions",
        "customer_behavior": "challenging",
        "outcome": "neutral",
        "special_tags": ["(transfer)"]
    },
    {
        "id": "agent_challenge_customer_emotional",
        "name": "Customer becomes very emotional",
        "description": "Customer crying or having breakdown",
        "customer_behavior": "vulnerable",
        "outcome": "neutral",
        "special_tags": ["(callback)"]
    },
    {
        "id": "agent_challenge_customer_drunk",
        "name": "Customer appears intoxicated",
        "description": "Customer seems under influence",
        "customer_behavior": "impaired",
        "outcome": "neutral",
        "special_tags": ["(callback)"]
    },
    {
        "id": "agent_challenge_customer_paranoid",
        "name": "Customer seems paranoid",
        "description": "Customer suspicious of everything",
        "customer_behavior": "suspicious",
        "outcome": "negative",
        "special_tags": ["(disconnect)"]
    },
    {
        "id": "agent_challenge_customer_rambling",
        "name": "Customer rambles off topic",
        "description": "Customer talks about unrelated things",
        "customer_behavior": "distracted",
        "outcome": "neutral",
        "special_tags": ["(function_1)"]
    },
    {
        "id": "agent_challenge_customer_demands_proof",
        "name": "Customer demands extensive proof",
        "description": "Customer wants detailed documentation",
        "customer_behavior": "challenging",
        "outcome": "neutral",
        "special_tags": ["(transfer)"]
    },

    # Escalation Scenarios (71-80)
    {
        "id": "escalation_supervisor_request",
        "name": "Customer requests supervisor",
        "description": "Customer wants to speak with manager",
        "customer_behavior": "escalating",
        "outcome": "transfer",
        "special_tags": ["(transfer)"]
    },
    {
        "id": "escalation_complaint_filing",
        "name": "Customer filing formal complaint",
        "description": "Customer wants to file official complaint",
        "customer_behavior": "escalating",
        "outcome": "transfer",
        "special_tags": ["(transfer)"]
    },
    {
        "id": "escalation_regulatory_threat",
        "name": "Customer threatens regulatory action",
        "description": "Customer mentions CFPB or state regulators",
        "customer_behavior": "escalating",
        "outcome": "transfer",
        "special_tags": ["(transfer)"]
    },
    {
        "id": "escalation_legal_department",
        "name": "Customer wants legal department",
        "description": "Customer demands to speak with legal",
        "customer_behavior": "escalating",
        "outcome": "transfer",
        "special_tags": ["(transfer)"]
    },
    {
        "id": "escalation_corporate_office",
        "name": "Customer wants corporate office",
        "description": "Customer demands corporate contact info",
        "customer_behavior": "escalating",
        "outcome": "transfer",
        "special_tags": ["(transfer)"]
    },
    {
        "id": "escalation_media_contact",
        "name": "Customer mentions media contact",
        "description": "Customer threatens news or social media",
        "customer_behavior": "escalating",
        "outcome": "transfer",
        "special_tags": ["(transfer)"]
    },
    {
        "id": "escalation_attorney_general",
        "name": "Customer mentions attorney general",
        "description": "Customer threatens state AG complaint",
        "customer_behavior": "escalating",
        "outcome": "transfer",
        "special_tags": ["(transfer)"]
    },
    {
        "id": "escalation_better_business_bureau",
        "name": "Customer mentions BBB complaint",
        "description": "Customer threatens BBB filing",
        "customer_behavior": "escalating",
        "outcome": "transfer",
        "special_tags": ["(transfer)"]
    },
    {
        "id": "escalation_lawsuit_threat",
        "name": "Customer threatens lawsuit",
        "description": "Customer threatens to sue company",
        "customer_behavior": "escalating",
        "outcome": "transfer",
        "special_tags": ["(transfer)"]
    },
    {
        "id": "escalation_police_threat",
        "name": "Customer threatens to call police",
        "description": "Customer threatens police involvement",
        "customer_behavior": "escalating",
        "outcome": "transfer",
        "special_tags": ["(transfer)"]
    },

    # Verification Issues (81-90)
    {
        "id": "verification_identity_failed",
        "name": "Customer fails identity verification",
        "description": "Customer cannot verify personal information",
        "customer_behavior": "suspicious",
        "outcome": "negative",
        "special_tags": ["(transfer)"]
    },
    {
        "id": "verification_refuses_to_verify",
        "name": "Customer refuses verification",
        "description": "Customer won't provide verification info",
        "customer_behavior": "uncooperative",
        "outcome": "negative",
        "special_tags": ["(disconnect)"]
    },
    {
        "id": "verification_partial_information",
        "name": "Customer provides partial verification",
        "description": "Customer gives some but not all required info",
        "customer_behavior": "suspicious",
        "outcome": "neutral",
        "special_tags": ["(transfer)"]
    },
    {
        "id": "verification_outdated_information",
        "name": "Customer information is outdated",
        "description": "Customer's info in system is old",
        "customer_behavior": "cooperative",
        "outcome": "positive",
        "special_tags": ["(function_1)"]
    },
    {
        "id": "verification_name_change",
        "name": "Customer changed name",
        "description": "Customer married/divorced, name changed",
        "customer_behavior": "cooperative",
        "outcome": "positive",
        "special_tags": ["(function_1)"]
    },
    {
        "id": "verification_ssn_mismatch",
        "name": "SSN doesn't match records",
        "description": "Social security number discrepancy",
        "customer_behavior": "suspicious",
        "outcome": "negative",
        "special_tags": ["(transfer)"]
    },
    {
        "id": "verification_address_mismatch",
        "name": "Address doesn't match",
        "description": "Customer address different from records",
        "customer_behavior": "cooperative",
        "outcome": "neutral",
        "special_tags": ["(function_1)"]
    },
    {
        "id": "verification_phone_mismatch",
        "name": "Phone number doesn't match",
        "description": "Customer phone different from records",
        "customer_behavior": "cooperative",
        "outcome": "neutral",
        "special_tags": ["(function_1)"]
    },
    {
        "id": "verification_dob_mismatch",
        "name": "Date of birth doesn't match",
        "description": "Birth date discrepancy in records",
        "customer_behavior": "suspicious",
        "outcome": "negative",
        "special_tags": ["(transfer)"]
    },
    {
        "id": "verification_multiple_attempts",
        "name": "Multiple failed verification attempts",
        "description": "Customer failed verification multiple times",
        "customer_behavior": "suspicious",
        "outcome": "negative",
        "special_tags": ["(transfer)"]
    },

    # Miscellaneous Edge Cases (91-100)
    {
        "id": "misc_customer_very_polite",
        "name": "Customer extremely polite and cooperative",
        "description": "Customer is unusually polite and helpful",
        "customer_behavior": "cooperative",
        "outcome": "positive",
        "special_tags": ["(function_1)"]
    },
    {
        "id": "misc_customer_suspicious_questions",
        "name": "Customer asks suspicious questions",
        "description": "Customer asking unusual questions about company",
        "customer_behavior": "suspicious",
        "outcome": "neutral",
        "special_tags": ["(transfer)"]
    },
    {
        "id": "misc_customer_recording_announcement",
        "name": "Customer announces recording",
        "description": "Customer states they are recording call",
        "customer_behavior": "legal",
        "outcome": "neutral",
        "special_tags": ["(function_1)"]
    },
    {
        "id": "misc_wrong_debt_amount_system",
        "name": "System shows wrong debt amount",
        "description": "Amount in system doesn't match customer's records",
        "customer_behavior": "disputing",
        "outcome": "dispute",
        "special_tags": ["(transfer)"]
    },
    {
        "id": "misc_duplicate_call_same_day",
        "name": "Customer already called today",
        "description": "Customer received multiple calls same day",
        "customer_behavior": "frustrated",
        "outcome": "negative",
        "special_tags": ["(transfer)"]
    },
    {
        "id": "misc_wrong_customer_name_system",
        "name": "Wrong customer name in system",
        "description": "System has incorrect name for customer",
        "customer_behavior": "confused",
        "outcome": "neutral",
        "special_tags": ["(transfer)"]
    },
    {
        "id": "misc_customer_moved_no_forwarding",
        "name": "Customer moved without forwarding info",
        "description": "Customer relocated, no contact information",
        "customer_behavior": "unavailable",
        "outcome": "neutral",
        "special_tags": ["(transfer)"]
    },
    {
        "id": "misc_background_noise_loud",
        "name": "Loud background noise",
        "description": "Customer in noisy environment",
        "customer_behavior": "environmental",
        "outcome": "neutral",
        "special_tags": ["(function_1)"]
    },
    {
        "id": "misc_customer_multitasking_distracted",
        "name": "Customer is multitasking",
        "description": "Customer distracted, doing other things",
        "customer_behavior": "distracted",
        "outcome": "neutral",
        "special_tags": ["(function_1)"]
    },
    {
        "id": "misc_perfect_resolution",
        "name": "Perfect customer interaction",
        "description": "Customer is ideal - polite, pays immediately",
        "customer_behavior": "ideal",
        "outcome": "positive",
        "special_tags": ["(function_1)"]
    },

    # BROKEN PROMISE SCENARIOS (101-110)
    {
        "id": "broken_promise_recent",
        "name": "Customer broke recent payment promise",
        "description": "Customer promised to pay last week but didn't follow through",
        "customer_behavior": "defensive",
        "outcome": "negative",
        "special_tags": ["(function_2)"]
    },
    {
        "id": "broken_promise_multiple",
        "name": "Customer broke multiple promises",
        "description": "Customer has history of making and breaking payment promises",
        "customer_behavior": "uncooperative",
        "outcome": "negative",
        "special_tags": ["(escalate)"]
    },
    {
        "id": "broken_promise_circumstances_changed",
        "name": "Broken promise due to changed circumstances",
        "description": "Customer made promise but circumstances changed (job loss, emergency)",
        "customer_behavior": "apologetic",
        "outcome": "neutral",
        "special_tags": ["(function_1)"]
    },
    {
        "id": "broken_promise_forgot",
        "name": "Customer forgot about payment promise",
        "description": "Customer genuinely forgot about their payment commitment",
        "customer_behavior": "confused",
        "outcome": "positive",
        "special_tags": ["(function_1)"]
    },
    {
        "id": "broken_promise_disputes_making",
        "name": "Customer disputes previous promise",
        "description": "Customer claims they never made the payment promise",
        "customer_behavior": "hostile",
        "outcome": "dispute",
        "special_tags": ["(transfer)"]
    },
    {
        "id": "broken_promise_partial_kept",
        "name": "Customer partially kept promise",
        "description": "Customer paid some but not the full promised amount",
        "customer_behavior": "cooperative",
        "outcome": "neutral",
        "special_tags": ["(function_2)"]
    },
    {
        "id": "broken_promise_technical_failure",
        "name": "Promise broken due to technical issue",
        "description": "Customer tried to pay but payment failed due to technical problems",
        "customer_behavior": "frustrated",
        "outcome": "positive",
        "special_tags": ["(function_1)"]
    },
    {
        "id": "broken_promise_bank_issue",
        "name": "Promise broken due to bank issue",
        "description": "Customer's payment failed due to insufficient funds or bank problems",
        "customer_behavior": "embarrassed",
        "outcome": "neutral",
        "special_tags": ["(function_1)"]
    },
    {
        "id": "broken_promise_family_emergency",
        "name": "Promise broken due to family emergency",
        "description": "Customer couldn't pay due to unexpected family emergency",
        "customer_behavior": "distressed",
        "outcome": "neutral",
        "special_tags": ["(function_1)"]
    },
    {
        "id": "broken_promise_wants_new_plan",
        "name": "Customer wants new payment plan after broken promise",
        "description": "Customer broke promise but wants to set up new payment arrangement",
        "customer_behavior": "negotiating",
        "outcome": "positive",
        "special_tags": ["(function_2)"]
    },

    # PROMISE TO PAY WITH DATA CONFIRMATION SCENARIOS (111-120)
    {
        "id": "promise_to_pay_date_confirmation",
        "name": "Customer making payment promise with specific date",
        "description": "Customer commits to pay by specific date and confirms details",
        "customer_behavior": "cooperative",
        "outcome": "positive",
        "special_tags": ["(function_1)", "(callback)"]
    },
    {
        "id": "promise_to_pay_method_confirmation",
        "name": "Customer providing payment method for promise",
        "description": "Customer confirms payment method (card, bank transfer, etc.) for future payment",
        "customer_behavior": "cooperative",
        "outcome": "positive",
        "special_tags": ["(function_2)"]
    },
    {
        "id": "promise_to_pay_contact_update",
        "name": "Customer updating contact info with payment promise",
        "description": "Customer provides updated contact information and makes payment commitment",
        "customer_behavior": "cooperative",
        "outcome": "positive",
        "special_tags": ["(function_1)"]
    },
    {
        "id": "promise_to_pay_payment_plan_setup",
        "name": "Customer setting up payment plan with dates",
        "description": "Customer agrees to payment plan with specific dates and amounts",
        "customer_behavior": "negotiating",
        "outcome": "positive",
        "special_tags": ["(function_2)", "(callback)"]
    },
    {
        "id": "promise_to_pay_bank_details",
        "name": "Customer providing bank details for payment",
        "description": "Customer gives bank account details for future payment processing",
        "customer_behavior": "cooperative",
        "outcome": "positive",
        "special_tags": ["(function_2)"]
    },
    {
        "id": "promise_to_pay_partial_plan",
        "name": "Customer promising partial payments with schedule",
        "description": "Customer commits to series of partial payments with confirmed dates",
        "customer_behavior": "negotiating",
        "outcome": "positive",
        "special_tags": ["(function_2)", "(callback)"]
    },
    {
        "id": "promise_to_pay_after_new_job",
        "name": "Customer promising payment after new job starts",
        "description": "Customer commits to pay after starting new job, provides start date",
        "customer_behavior": "hopeful",
        "outcome": "neutral",
        "special_tags": ["(callback)"]
    },
    {
        "id": "promise_to_pay_insurance_settlement",
        "name": "Customer promising payment from insurance settlement",
        "description": "Customer expects insurance money and commits to pay from settlement",
        "customer_behavior": "cooperative",
        "outcome": "neutral",
        "special_tags": ["(callback)"]
    },
    {
        "id": "promise_to_pay_tax_refund",
        "name": "Customer promising payment from tax refund",
        "description": "Customer commits to pay when tax refund arrives, provides timeline",
        "customer_behavior": "cooperative",
        "outcome": "positive",
        "special_tags": ["(function_1)", "(callback)"]
    },
    {
        "id": "promise_to_pay_verification_required",
        "name": "Customer making promise but needs identity verification",
        "description": "Customer wants to make payment promise but needs to verify identity first",
        "customer_behavior": "cooperative",
        "outcome": "neutral",
        "special_tags": ["(transfer)"]
    },

    # CRITICAL EDGE CASES (121-130)
    {
        "id": "edge_case_wrong_account_payment",
        "name": "Customer paid to wrong account",
        "description": "Customer made payment but to wrong account number or company",
        "customer_behavior": "confused",
        "outcome": "neutral",
        "special_tags": ["(transfer)"]
    },
    {
        "id": "edge_case_unrecorded_payment",
        "name": "Customer made payment but system didn't record",
        "description": "Customer claims payment was made but not showing in system",
        "customer_behavior": "frustrated",
        "outcome": "dispute",
        "special_tags": ["(transfer)"]
    },
    {
        "id": "edge_case_bankruptcy_proceedings",
        "name": "Customer in bankruptcy proceedings",
        "description": "Customer is currently in bankruptcy and cannot make payments",
        "customer_behavior": "legal",
        "outcome": "legal",
        "special_tags": ["(transfer)"]
    },
    {
        "id": "edge_case_deceased_customer_family",
        "name": "Customer is deceased - next of kin",
        "description": "Family member informs that customer has passed away",
        "customer_behavior": "wrong_person",
        "outcome": "legal",
        "special_tags": ["(transfer)"]
    },
    {
        "id": "edge_case_military_deployment",
        "name": "Customer deployed in military",
        "description": "Customer is on military deployment and cannot access funds",
        "customer_behavior": "vulnerable",
        "outcome": "legal",
        "special_tags": ["(transfer)"]
    },
    {
        "id": "edge_case_incarcerated_customer",
        "name": "Customer is incarcerated",
        "description": "Customer is in jail/prison and cannot make payments",
        "customer_behavior": "vulnerable",
        "outcome": "legal",
        "special_tags": ["(transfer)"]
    },
    {
        "id": "edge_case_identity_theft_victim",
        "name": "Customer claims identity theft",
        "description": "Customer claims the debt is result of identity theft",
        "customer_behavior": "disputing",
        "outcome": "dispute",
        "special_tags": ["(transfer)"]
    },
    {
        "id": "edge_case_elderly_confused_customer",
        "name": "Elderly customer with confusion",
        "description": "Elderly customer seems confused about debt and situation",
        "customer_behavior": "vulnerable",
        "outcome": "neutral",
        "special_tags": ["(transfer)"]
    },
    {
        "id": "edge_case_language_barrier_customer",
        "name": "Customer has language barrier",
        "description": "Customer doesn't speak language well, needs interpreter",
        "customer_behavior": "confused",
        "outcome": "neutral",
        "special_tags": ["(transfer)"]
    },
    {
        "id": "edge_case_hearing_impaired_customer",
        "name": "Customer is hearing impaired",
        "description": "Customer has hearing difficulties and needs accommodation",
        "customer_behavior": "vulnerable",
        "outcome": "neutral",
        "special_tags": ["(transfer)"]
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
    "hostile": "Customer is angry or aggressive",
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
