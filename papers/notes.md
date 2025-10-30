Notes and manuscript for assignment
# Significant-Loophole-Free Test of Bell's Theorem with Entangled Photons
## The Purpose
According to some early 1900's scientist quantum mechanics is not plausible, and they propsed a *local realism* worldview. Here "*local*" means that no information can travel as speeds exceeding the speed of light, and "*realism*" means that previous to the measurement the physical properties of a state is defined. If this worldview holds true, then a correlation between two measurements can never exceed a certain value; this leads to the definition of Bell's inequality. The goal for the Bell's test is to utilized quantum mechanics to 'break' this inequality - that is achieve results that classical *local realism* dictates is impossible.

In this paper, the authors used a Claus-Horne-Ebhard (CH-E) inequality, requiring only one photon detector per observer (Alice/Bob):
$$
    J \equiv p_{++}(a_1b_1) - p_{+0}(a_1b_2) - p_{0+}(a_2b_1) - p_{00}(a_2b_2) \leq 0.
$$
The first subscript is the outcome of the detector being a detection, "+", or no detection, "0", for observer Alice, and the second is likewise for the observer "Bob". The arguments are the measurement setting for Alice and Bob respectively, $a_i,b_i$.

According to quantum mechanics, an entagled state can violate the inequality, and the authors use:
$$
    \ket{\Psi} = \frac{1}{\sqrt{1 + r^2}}\left(\ket{0}_A\ket{1}_B + r\ket{1}_A\ket{0}_B\right).
$$  
Note, that in the paper the authors use "V" to denote the vertical polarized light, and "H" to denote horizontal polarized light. Here we have used the notation from the lectures and the notes from Aaronson (0 and 1).

## Loopholes
Some critique you might pose the experiment is the *loopholes* wich could explain the results from a local realism POV. To redeem these loopholes, the experiment has to address the loopholes all at the same time.

### The locality loophole
Also known as the communication loophole, states that the settings choice of a measurement could be communcated to the other observer to influence the measurement result. To aviod this, the authors use space-like separation. The observers has to be separeted so far apart, that one observes settings choice could not be communicated, even with a light-speed signal, to the other observer before the measurement was taken.

This is neatly shown in the space-time diagram of fig. 2 in the article.

### The freedom-of-choice loophole
This loophole states that the settings choice could be influenced by the properties of the system (the emission of the entagled state). To close this loophole the authors, again, use space-like separation of the photon emission and the settings choice for each oberser.

Again, this is shown in the space-time diagram of fig. 2.

### The fair-sampling loophole
This loophole indicates that a subset of data might violate Bell's inequality, whereas the whole ensamble does not. This loophole can be closed by having high detector efficincies. The authors also propose that violating a Bell's inequality that does not assume a "fair-sampling" would be even better.

## The setup
### Generating entaglement
Fig. 1 shows the setup. The authors use Spontaneous parametric down-conversion, which is eluminating a non-linear crystal by some high frequency laser, and the crystal then has a probability of creating two photons of lower frequency; ofcourse conservation of energy/momentum is satisfied. This is done by using a source laser of 405 nm wavelength, to excite a periodically poled crystal (ppKTP) to create 2 polarization entagled photons of 810 nm; and is then send to each observer (Alice/Bob).

### Measuring the photons.
Each observer (Alice/Bob) has a random number generator (RNG). The RNG works by creating 4 "raw" bits from the phase of an optical pulse, and then computing the parity (XOR'ing the 4 raw bits) to create a single random bit. The single random bit is then delivered to a electro-optical modulator (EOM) that switched the polarization rotator in front of a polarized beam-splitter (PBS). This way the EOM can have one of two settings for the signal photon: horizontal or vertical, and then the photon is either a "detection" event or a "no detection" event.

After the EOM, the signal is passed through a PBS - the transmitted photons passed to a transission-edge sensor (TES), and the reflected photons sent to a detector. The reflected photons is used for determining the the time it takes for a photon to travel from the source to the TES. The The TES is in serial with a superconducting quantum interference sensor (SQUID), and together they can measure the photon detection events. The readout signal from the TES depends on the photon energy/wavelength, and the operator can therefore easily distinguish between detection events and background light. This signal processing is done using a digitizer/PC-setup.

All the components have a local clock timer to time the setting choice, detection etc.

