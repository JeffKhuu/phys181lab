#set page(
  header: [#h(1fr) Jeff Khuu - Experimental Design Document],
  numbering: "1"
)

#title[Measuring the Deviations from Simple Harmonic Motion of a Pendulum]

= Introduction
This experiment focuses on analyzing the motion of a pendulum, specifically when the pendulum's bob is released far from its equilibrium point. At these positions, the motion of the pendulum becomes much harder to predict analytically as the linear relationship between force and displacement described by Hooke's Law using the small angle approximation begins to deviate.

Developing a sophisticated model of a pendulum which accurately describes the mechanics of its non-linear motion has been the focus of renowned physicists like Christiaan Huygens and Leonhard Euler. With such a model of harmonic motion being prevalent to areas such as springs and oscillators in physical systems to wave propagation, radiation of light and particle physics. By studying the non-simple harmonic motion of a pendulum we better our understanding of classical mechanics and shed light on the motivations behind the mathematical and numerical methods used in modern physics to model complex behaviour.

The goal of this experiment is to determine the angle at which simple harmonic motion and the small angle approximation begin to deviate drastically determined by a set threshold error. To do so we will analyze both the period and energy of a pendulum taken at increasing starting angles to compare with the period and energy as predicted by simple harmonic motion. We hypothesize simple harmonic motion will begin to deviate significantly around $approx 20degree$, at this point the percent error for the small angle approximation of $sin$ reaches above $2%$. Additionally, we will develop a computer simulation of a pendulum using modern numerical methods to avoid the small angle approximation to show that this fits our experimentally determined values much more accurately.

= Materials / Equipment / Setup
The required materials to complete this experiment include:
- Scale & Meter Stick
- String
- Fixed Rod, Adjustable Clamp & Protractor
- Hanging Mass
- Smartphone

#figure(caption: "Diagrams of Initial Experimental Setup (Sideview & Frontview)")[
  #grid(
    columns: 2,
    align: center + horizon,
    gutter: 1em,
    image("experimentdesign-side.svg", width: 100%), image("experimentaldesign-front.svg", width: 60%),
  )
]


= Design (Error & Bias)
Some possible sources of error and uncertainty come from measuring the angle of release for each trial, friction and air resistance dampening the oscillation of the pendulum, precession of the pendulum bob outside of the plane of motion and motion blur affecting the video analysis.
To ensure an accurate measurement of angle we fix a protractor as part of our pendulum setup. To account for the effects of dampening, we will take and analyze a trial with the bob released close to equilibrium to determine a dampening constant that we will use to determine our theoretical values. To prevent the precession of the pendulum bob, we utilize the adjustable clamp and attempt to release the mass parallel to the intended plane of motion, taking multiple measurements if necessary. Finally, we attempt to mitigate motion blur by taking higher frame per second video and utilize a string with greatest possible length to increase the period of the oscillation (decreasing the angular velocity).

= Timeline & Procedure
#figure(caption: "Timeline of Experiment")[
  #image("experimentaldesign-timeline.svg", width: 95%)
]
*Timeline*
- *Week 4*: Complete Design Document.
- *Week 6*: Take and analyze data, begin working on computer pendulum simulation and implementation of Runge-Katta method.
- *Week 7*: Retake data if necessary, complete analysis on data. Continue work on computer pendulum simulation comparing simulation to experimental data.
- *Week 8*: Complete computer pendulum simulation. Work on presentation and report completing up to the _Methods_ section.
- *Week 9*: Work on presentation and report.
- *Week 10*: Submit lab report and prepare for presentation.
- *Week 11*: Present to groups during lab session.


*To take data and complete the experiment:*
+ Measure the length of the pendulum's string using the meter stick and the mass of the pendulum's bob (hanging mass) using the scale.
+ Setup the pendulum and smartphone as diagrammed, making sure to keep the smartphone parallel to the plane of motion.
+ Perform seven trials starting from an initial angle $theta = 10degree$ before continuing from $theta = 15 degree$ until $theta = 90degree$ (horizontal) through $15 degree$ increments using the smartphone's camera to record each trial.
+ Analyze the motion of the pendulum for the trial at $theta = 10degree$ using video analysis software such as Tracker or Logger Pro to determine a dampening constant.
+ Analyze the motion of each trial and compare the period and potential energy to the computer simulated expected values to find the threshold at which simple harmonic motion deviates.

= Chronicling Strategy
Measurements will be taken in the form of video to be analyzed later on. Analysis and data extracted from measurements will be stored as Tracker files and `.csv` files.
All data, measurements, reports and source code will be chronicled and versioned remotely using Git source control and made publicly available using GitHub. Full repository available at #link("https://github.com/JeffKhuu/phys181lab")
