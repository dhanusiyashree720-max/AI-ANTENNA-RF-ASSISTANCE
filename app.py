
import math
import streamlit as st

st.set_page_config(
    page_title="AI Antenna & RF Learning Assistant",
    page_icon="📡",
    layout="wide"
)

st.title("📡 AI Antenna and RF Concepts Learning Assistant")
st.write(
    "Learn antenna and RF fundamentals with formulas, "
    "worked examples, and engineering verification."
)

st.info(
    "Engineering note: AI-generated answers must be checked "
    "against reliable references. This application uses "
    "deterministic equations for its built-in calculations."
)

topics = [
    "Dipole Antenna",
    "Antenna Gain",
    "Impedance Matching",
    "VSWR",
    "Link Budget"
]

page = st.sidebar.selectbox(
    "Choose a learning module",
    [
        "Home",
        "RF Lessons",
        "Formula Calculator",
        "Numerical Problems",
        "Glossary",
        "Quiz",
        "Verification Report"
    ]
)

C = 299792458  # Speed of light in m/s


if page == "Home":
    st.header("Welcome to RF Learning")

    st.write("Explore five essential RF engineering topics.")

    for topic in topics:
        st.markdown(f"- **{topic}**")

    st.subheader("Project objectives")
    st.write("""
    - Learn beginner and advanced RF concepts.
    - Check formulas and engineering units.
    - Solve numerical problems.
    - Calculate a wireless link budget.
    - Identify possible AI-generated errors.
    """)

    st.subheader("Reference starting points")
    st.markdown(
        "- [ITU-R Recommendations](https://www.itu.int/rec/R-REC/en)"
    )
    st.markdown(
        "- [ARRL — The National Association for Amateur Radio]"
        "(https://www.arrl.org/)"
    )
    st.markdown(
        "- [NIST — Reference on Constants](https://physics.nist.gov/cuu/Constants/)"
    )


elif page == "RF Lessons":
    topic = st.selectbox("Select a topic", topics)

    lessons = {
        "Dipole Antenna": (
            "A dipole antenna is a conductor antenna commonly "
            "made of two arms. A half-wave dipole has an approximate "
            "total length of half a wavelength.",
            "L ≈ λ/2",
            "λ = c/f"
        ),
        "Antenna Gain": (
            "Antenna gain describes how effectively an antenna "
            "radiates or receives power in a specified direction "
            "compared with a reference antenna.",
            "G(dBi) = 10 log10(Glinear)",
            "Gain in dBi is referenced to an isotropic antenna."
        ),
        "Impedance Matching": (
            "Impedance matching reduces reflections between a "
            "source and load. For a real reference impedance, "
            "maximum power transfer occurs when the load equals "
            "the complex conjugate of the source impedance.",
            "Γ = (ZL - Z0)/(ZL + Z0)",
            "This reflection equation assumes a real Z0."
        ),
        "VSWR": (
            "Voltage Standing Wave Ratio describes the standing "
            "wave caused by reflections on a transmission line.",
            "VSWR = (1 + |Γ|)/(1 - |Γ|)",
            "For passive loads, 0 ≤ |Γ| ≤ 1. VSWR is infinite "
            "when |Γ| = 1."
        ),
        "Link Budget": (
            "A link budget estimates received power by adding "
            "transmitter power and antenna gains, then subtracting "
            "propagation and system losses.",
            "Pr(dBm) = Pt(dBm) + Gt(dBi) + Gr(dBi) - losses(dB)",
            "Include free-space path loss and other applicable "
            "losses in the total losses."
        )
    }

    explanation, formula, note = lessons[topic]

    st.subheader(topic)
    st.write(explanation)
    st.latex(formula)
    st.caption(note)

    st.warning(
        "Verify formulas and assumptions against a trusted "
        "engineering reference before using them in real designs."
    )


elif page == "Formula Calculator":
    st.header("RF Formula Calculator")

    mode = st.selectbox(
        "Choose calculation",
        [
            "Wavelength",
            "VSWR",
            "Return Loss",
            "Reflection Coefficient"
        ]
    )

    if mode == "Wavelength":
        f = st.number_input(
            "Frequency (MHz)", min_value=0.001, value=100.0
        )
        if st.button("Calculate wavelength"):
            wavelength = C / (f * 1e6)
            st.success(f"Wavelength = {wavelength:.6f} m")
            st.write(f"Half wavelength ≈ {wavelength / 2:.6f} m")

    elif mode == "VSWR":
        gamma = st.number_input(
            "Reflection coefficient magnitude |Γ|",
            min_value=0.0,
            max_value=1.0,
            value=0.2
        )
        if st.button("Calculate VSWR"):
            if gamma == 1:
                st.error("VSWR is infinite for |Γ| = 1.")
            else:
                vswr = (1 + gamma) / (1 - gamma)
                st.success(f"VSWR = {vswr:.4f}:1")

    elif mode == "Return Loss":
        gamma = st.number_input(
            "|Γ| (must be greater than zero and at most 1)",
            min_value=0.001,
            max_value=1.0,
            value=0.2
        )
        if st.button("Calculate return loss"):
            rl = -20 * math.log10(gamma)
            st.success(f"Return Loss = {rl:.4f} dB")

    else:
        z0 = st.number_input(
            "Real reference impedance Z0 (ohms)",
            min_value=0.001,
            value=50.0
        )
        r = st.number_input("Load resistance (ohms)", min_value=0.0, value=75.0)
        x = st.number_input("Load reactance (ohms)", value=0.0)

        if st.button("Calculate reflection coefficient"):
            numerator = complex(r - z0, x)
            denominator = complex(r + z0, x)

            gamma_complex = numerator / denominator
            st.write(f"Γ = {gamma_complex.real:.4f} + "
                     f"j({gamma_complex.imag:.4f})")
            st.write(f"|Γ| = {abs(gamma_complex):.4f}")


elif page == "Numerical Problems":
    st.header("Worked Numerical Examples")

    st.subheader("Problem 1: Wavelength")
    st.write("Find the wavelength at 100 MHz in free space.")
    st.latex(r"\lambda = \frac{c}{f}")

    if st.button("Show wavelength solution"):
        result = C / 100e6
        st.write("Substitute c = 299,792,458 m/s.")
        st.write("f = 100,000,000 Hz.")
        st.success(f"Answer: λ = {result:.6f} m")

    st.divider()

    st.subheader("Problem 2: VSWR")
    st.write("Find VSWR when |Γ| = 0.2.")
    st.latex(r"VSWR = \frac{1+|\Gamma|}{1-|\Gamma|}")

    if st.button("Show VSWR solution"):
        result = (1 + 0.2) / (1 - 0.2)
        st.write("Substitute |Γ| = 0.2.")
        st.success(f"Answer: VSWR = {result:.2f}:1")

    st.caption(
        "These are two initial examples, not the final set of "
        "eight manually verified problems."
    )


elif page == "Glossary":
    st.header("RF Glossary")

    glossary = {
        "Antenna": "A device that transmits or receives electromagnetic waves.",
        "Gain": "Directional radiation or reception effectiveness relative to a reference.",
        "Impedance": "The complex opposition a circuit presents to alternating current.",
        "Wavelength": "The spatial period of a wave.",
        "Frequency": "The number of wave cycles per second, measured in hertz.",
        "VSWR": "A measure of standing-wave severity on a transmission line.",
        "Reflection coefficient": "The complex ratio of reflected to incident wave amplitude.",
        "Return loss": "A logarithmic measure of reflected power relative to incident power.",
        "dB": "A logarithmic ratio of two power or amplitude quantities.",
        "dBm": "Absolute power expressed in decibels relative to 1 milliwatt.",
        "Link budget": "An accounting of gains and losses in a communication link."
    }

    for term, definition in glossary.items():
        with st.expander(term):
            st.write(definition)


elif page == "Quiz":
    st.header("RF Knowledge Quiz")

    questions = [
        ("What is the SI unit of frequency?", ["Hertz", "Ohm", "Watt"], 0),
        ("What is the speed of light approximately?", ["3 × 10^6 m/s", "3 × 10^8 m/s", "3 × 10^10 m/s"], 1),
        ("What is the unit of impedance?", ["Ohm", "Hertz", "dBm"], 0),
        ("What does VSWR describe?", ["Reflection-related standing waves", "Frequency only", "Temperature"], 0),
        ("What is the free-space wavelength formula?", ["c/f", "f/c", "c × f"], 0),
        ("What is the reference power for dBm?", ["1 W", "1 mW", "1 kW"], 1),
        ("What is the ideal VSWR for a matched line?", ["0:1", "1:1", "2:1"], 1),
        ("What does dBi reference?", ["An isotropic antenna", "A dipole only", "One milliwatt"], 0),
        ("What does a link budget estimate?", ["Received power", "Battery colour", "Antenna mass only"], 0),
        ("What is the symbol commonly used for reflection coefficient?", ["Γ", "λ", "μ"], 0)
    ]

    answers = []
    for i, (question, options, correct) in enumerate(questions):
        answer = st.radio(
            f"{i + 1}. {question}",
            options,
            key=f"quiz_{i}"
        )
        answers.append(options.index(answer))

    if st.button("Submit quiz"):
        score = sum(
            answers[i] == questions[i][2]
            for i in range(len(questions))
        )
        st.success(f"Your score: {score}/10")
        with st.expander("Verified answer key"):
            for i, (q, options, correct) in enumerate(questions):
                st.write(f"{i + 1}. {options[correct]}")


elif page == "Verification Report":
    st.header("Verification and Limitations")

    st.write("""
    Verification checklist:

    1. Compare definitions with reliable engineering references.
    2. Check equation assumptions and valid input ranges.
    3. Recalculate numerical answers independently.
    4. Confirm all units and significant figures.
    5. Record errors instead of silently changing results.
    6. Never treat an AI-generated citation as verified until
       the referenced source has been opened and checked.
    """)

    st.subheader("Known limitations")
    st.write("""
    - This starter application does not use a live AI model.
    - Its two worked numerical examples are not a complete
      eight-problem verification set.
    - It does not simulate a real antenna or electromagnetic field.
    - Calculator results depend on correct user inputs and assumptions.
    - Its reference links are starting points, not proof that
      every equation has already been checked.
    """)

    st.subheader("Verification log template")
    st.text_area(
        "Record an error or verification result",
        placeholder=(
            "Problem ID, reference, AI result, manual result, "
            "units, error type, correction"
        )
    )

    st.caption(
        "This log is not saved permanently in this starter version."
    )

st.divider()
st.caption(
    "AI Antenna & RF Learning Assistant | Educational prototype"
)
