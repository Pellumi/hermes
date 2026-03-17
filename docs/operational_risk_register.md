ADOS Operational & Risk Register  
Pre-Implementation Risk Baseline

Scope: Simulation → Supervised Abuja Pilot  
Status: Final \- Approved for implementation  
Last Updated: February 17, 2026  
Next Review: Monthly, or after any safety incident

1. Risk Classification Framework

Each risk is categorized by:

| Attribute | Description |
| :---- | :---- |
| Uncertainty | What we do not know |
| Assumption | What we are currently assuming |
| No Proof Yet | What has no empirical validation |
| Likelihood | 1 (Rare) to 5 (Almost Certain) |
| Impact | 1 (Minor) to 5 (Existential) |
| Risk Score | Likelihood \* Impact |
| Priority | CRITICAL (15-25), HIGH (10-14), MEDIUM (5-9), LOW (1-4) |
| Mitigation Strategy  | Actions to rescue likelihood or impact |
| Prototype Experiment | Test to validate assumptions |
| Validation Criteria | Success metrics for closure |
| Owner | Responsible party |
| Due Date | When mitigation must be complete |

2. Core Systemic Uncertainties

Before specific risks, these are global unknowns that underpin the entire architecture:  
Urban Airspace Behavior in Abuja

* Uncertainty: Regulatory stance on semi-autonomous BVLOS; restrictions near Nnamdi Azikiwe Airport; millitary/government geofencing data completeness; Harmattan visibility compliance  
* Assumption: 120m AGL ceiling acceptable; Abuja zones can be statisstically geofenced; NCAA approval pathway viable  
* No Proof Yet; Dynamic airspace updates; real enforcement mechanisma; emergency landing legality in urban zones  
* Impace: Existential

  Real Battery Behaviour Under Load

* Uncertainty: True energy consumption under 8kg payload; wind amplification effects; heat degradation in Abuja climate; battery aging curve under frequent cycles  
* Assumption: Reserve buffer of 30% is sufficient; diversion safety margin calculation is valid; linear-ish regression model approximates reality  
* No Proof Yet: Multi-leg energy summation accuracy; real drain spikes \>15% deviation threshold; safe diversion threshold reliability  
* Impact: Existential

	Cellular Reliability at Operational Altitudes

* Uncertainty: Signal stability at 40-120m AGL; packet loss during tower handoff; Harmattan signal degradation; latency spikes under network congestion  
* Assumption: 4G sufficient; dead zones mappable; 30-second signal loss threshold workable  
* No Proof Yet: Reliable 1Hz streaming during flight; WebSocket scaling to concurrent observers; reconnect synchronization robustness  
* Impact: High

	Real-Time Rerouting Under Latency

* Uncertainty: Actual round-trip latency under load; computational cost of 3D A\* on dense grid; worst-case reroute chain events  
* Assumption: Grid size (50m \* 50m \* 10m) manageable; cost function scaling linear  
* No Proof Yet: 10+ reroutes per mission stress case; multi-drone concurrent route calculation  
* Impact: Medium-High

	Human Operator Response Time Under Stress

* Uncertainty: Can operators correctly interpret emergency situations under time pressure? Will they abort when they should, or override incorrectly? What’s the error rate of human decision-making in high-stress scenarios?  
* Assumption: Operators will follow protocols; training is sufficient; response times within escalation timeouts (2min Level 3, 30 sec Level 4\)  
* No Proof Yet: Actual operator performance under simulated emergencies; decision accuracy in ambiguous situations  
* Impact: High

3. Detailed Operational Risk Register

RISK 1 \- Battery Consumption Modeling

| Attribute | Value |
| :---- | :---- |
| Risk ID | R1 |
| Risk Name | Battery Model Error |
| Uncertainty | True energy consumption under 8kg payload; wind amplification effects; heat degradation; aging curve |
| Assumption | Reserve buffer 30% sufficient; diversion margin calculation valid; regression model approximates reality |
| No Proof Yet | Multi-leg energy summation; drain spikes \> 15%; diversion threshold reliability |
| Likelihood | 4 (Likely \- unknown factors) |
| Impact | 5 (Existential \- drones fail) |
| Risk Score | 20 |
| Priority | CRITICAL |

Mitigation Strategy

* Conservative energy multipliers in Phase 2 (1.2 \* base)  
* Overestimate wind effect by 15%  
* Increase safety margin from 25% → 35% for pilot  
* Limit maximum delivery radius initially (5km)  
* Track battery cycle count in drone\_registry  
* Recalibrate model every 50 cycles or 3 months  
* Implement adoptive thresholds based on battery health score

Prototype Experiment  
Battery Characterization Test (No Delivery)

* Fly empty drone at: 0kg, 4kg, 8kg payload  
* Measure: Wh/km, temperature drift, voltage sag  
* Conduct under: low wind, moderate wind, 35-40°C  
* Test batteries at different life stages: new, 50 cycles, 100 cycles  
* Minimum: 30 controlled flights per payload category

Validation Criteria

* Model error \<10% for batteries with \<50 cycles  
* Model error \<15% for batteries with 50-200 cycles  
* MOdel retraining triggered when error consistently \>12%  
* No unexpected voltage collapse  
* Diversion trigger accuracy \>=99%  
* Safe landing reserve \>=20% consistently

Owner: Battery Engineer  
Due Date: Before Phase 2 start

RISK 2 \- Abuja Airspace Constraints

| Attribute | Value |
| :---- | :---- |
| Risk ID | R2 |
| Risk Name | Regulatory Restrictions |
| Uncertainty | NCAA stance on BVLOS; airport restrictions; military geofencing; Harmattan visibility |
| Assumption | 120m AGL acceptable; static geofencing sufficient; NCAA approval pathway viable |
| No Proof Yet | Dynamic airspace updates; enforcement mechanisms; emergency landing legality |
| Likelihood | 3 (Possible \- active engagement needed) |
| Impact | 5 (Existential \- regulatory shutdown) |
| Risk Score | 15 |
| Priority | CRITICAL |

Mitigation Strategy

- Target NCAA Part 18.3.2 (Experimental Certificate) for Phase 2  
- Engage NCAA by Q2 2026 with preliminary flight test data  
- Restrict pilot flights to low-density zones (controlled campus, industrial areas)  
- Pre-map emergency landing zones with NEMA coordination  
- Prepare public communication strategy for any incident  
- Map all flights away from densely populated areas initially

Prototype Experiment  
Regulatory Sandbox Test

* 10 supervised flights in controller airspace  
* Document; flight logs, operator supervision, geofence compliance  
* Submit documentation to NCAA for feedback  
* Engage NEMA on emergency landing protocols

Validation Criteria

* Zero geofence violations  
* Documented approval pathway (Experimental Certificate)  
* Formal advisory or informal clearance from NCAA  
* Emergency landing zones approved by local authorities

Owner: Regulatory Lead  
Due Date: Ongoing \- update monthly

RISK 3 \- Telemetry Reliability Over Cellular Networks

| Attribute | Value |
| :---- | :---- |
| Risk ID | R3 |
| Risk Name | Cellular Instability |
| Uncertainty | Signal at 40-120m AGL; tower handoff packet loss; Harmattan degradation; congestion spikes |
| Assumption | 4G sufficient; dead zones mappable; 30s signal loss threshold workable |
| No Proof Yet  | 1Hz streaming reliability; WebSocket scaling; reconnect robustness |
| Likelihood | 4 (Likely \- urban cellular variable) |
| Impact | 4 (High \- loss of visibilty) |
| Risk Score | 16 |
| Priority  | CRITICAL |

Mitigation Strategy

- Dual-SIM redundancy (two different carriers)  
- Store-and-forward buffer onboard (up to 5 minutes)  
- Autonomous continuation policy per signal loss matrix  
- Degrade telemetry frequency when unstable (1Hz → 0.2Hz)  
- Cache critical state transitions for replay on reconnect

Prototype Experiment  
Cellular Flight Mapping Test

* Fly drone in grid across Abuja zones  
* Test at 8am, 12pm, 6pm, 10pm (peak vs off-peak)  
* Log: RSSI (dBm), latency, packet loss %, tower handovers  
* Simulate complete network loss: force disconnect, measure autonomous behavior  
* Test carrier handover: force switch between networks mid-flight  
* Minimum: 20 flight paths covering all major zones

Validation Criteria

* Signal \>= \-95 dBm for 95% of route  
* Packet loss \<2%  
* Reconnect time \<10 seconds  
* No single carrier provides \>90% coverage alone → require dual-SIM  
* Handover latency \<5 seconds  
* Autonomous mission continuation successful for up to 15minutes without signal  
* No mission aborted solely due to signal loss

Owner: Comms Engineer  
Due Date: Before Phase 2 start

RISK 4 \- Real-Time Rerouting Under Latency

| Attribute | Value |
| :---- | :---- |
| Risk ID | R4 |
| Risk Name | Reroute Latency |
| Uncertainty | Round-trip latency under load; A\* computation cost; worst-case reroute chains |
| Assumption | Grid size manageable; cost function scaling linear |
| No Proof Yet | 10+ reroutes per mission; multi-drone concurrent calculation |
| Likelihood | 3 (Possible \- design limit unknown) |
| Impact | 4 (High \- collision or energy error) |
| Risk Score | 12 |
| Priority | HIGH |

Mitigation Strategy

- Pre-compute route corridors (coarse grid)  
- Hierarchical routing: coarse (50m) for long distance, fine (10m) near obstacles  
- Limit recalculation scope to affected segments only  
- Cache route graph in memory (Redis)  
- Queue reroute requests with priority (emergency \> battery \> optimization)  
- Validate geofence data freshness with timestamp checks

Prototype Experiment  
Latency Stress Simulation

* 1000 simulated missions  
* Inject: wind spike events, no-fly zone updates, battery drain spikes  
* Simulate concurrent reroute storm: 20 drones requesting simultaneously  
* Measure: calculation time, end-to-end propagation, queue depth, amx wait time, failure rate

Validation Criteria

* 95% reroutes \<500ms  
* 99% reroutes \<1s  
* No mission stall due to routing  
* Concurrent storm: max wait time \<2s for all drones  
* If exceeded → move partial reroute logic to edge

Owner: Autonomy Lead  
Due Date: Before Phase 2 start

RISK 5 \- Payload Container Reliability

| Attribute | Value |
| :---- | :---- |
| Risk ID | R5 |
| Risk Name | Container Mechanical Faults |
| Uncertainty | Winch reliability under repeated cycles; lock failure frequency; weight sensor drift |
| Assumption | ±50g sensor accuracy; 3 retry attempts sufficient |
| No Proof Yet | 100+ cycle durability; environmental effects (heat, dust) |
| Likelihood | 2 (Unlikely \- but untested) |
| Impact | 3 (Medium \- mission failure) |
| Risk Score | 6 |
| Priority | MEDIUM |

Mitigation Strategy

- Bench cycle test: 1000 deployments minimum  
- Environmental chamber test: 100 cycles at 45°C, 90% humidity  
- Dust ingress test: simulate Harmattan conditions  
- Wireless link test: measure packet loss between container and drone at 5m  
- Weight sensor drift measurement every 100 cycles  
- Container firmware update capability for sensor calibration

Prototype Experiment  
Container Durability Test Suite

* 1000 mechanical cycles in lab conditions  
* 100 cycles at 45°C, 90% humidity  
* 100 cycles with dust exposure  
* 100 wireless transmissions at 5m distance  
* Measure: failure rate, accuracy drift, signal strength

Validation Criteria

* No mechanical failure in first 500 field cycles  
* Failure rate \<1% through 1000 cycles  
* Wireless link success rate \>99.5% at 5m  
* Weight sensor drift \< ±100g after 1000 cycles  
* Lock mechanism: 100% successful seal on command

Owner: Hardware Lead  
Due Data: Before Phase 2 start

RISK 6 \- Visual Identification Accuracy (Phase 3+)

| Attribute | Value |
| :---- | :---- |
| Risk ID | R6 |
| Risk Name | Visual ID Errors |
| Uncertainty | CV accuracy in varied demographics; lighting/weather effects; privacy compliance |
| Assumption | Can be deferred to Phase 3; NITDA guidance will be clearer |
| No Proof Yet | Real-world performance in Abuja conditions |
| Likelihood | 1 (Deferred \- not in Phase 1/2) |
| Impact | 3 (Medium \- misidentification risk) |
| Risk Score | 3  |
| Priority | LOW |

Mitigation Strategy

* Phase 1: Cameras active but not recording (live view only for operator escalations)  
* Phase 1: No visual data stored (explicitly in data retention policy)  
* Phase 2: Audio-only verification \+ OTP only  
* Phase 3 preparation: Operator training program, certification requirements  
* Privacy impact assessment before Phase 3

Validation Criteria (Phase 3\)

* CV confidence \>0.85 for 90% of identifications  
* Operator escalation rate \<10%  
* Privacy confirmed with NITDA

Owner: Product Manager  
Due Date: Re-evaluate Phase 3

RISK 7 \- Operator Error During Intervention

| Attribute | Value |
| :---- | :---- |
| Risk ID | R7 |
| Risk Name | Operator Error |
| Uncertainty | Can operators correctly interpret emergencies under time pressure? Will they abort appropriately or override incorrectly? |
| Assumption | Operators follow protocols; training is sufficient; response times within escalation timeouts |
| No Proof Yet | Actual operator performance under simulated emergencies; decision accuracy in ambiguous situations |
| Likelihood | 3 (Possible \- human factors) |
| Impact | 4 (High \- wrong decision could cause incident) |
| Risk Score | 12 |
| Priority | HIGH |

Mitigation Strategy

- Simulator training with realistic emergency scenarios (10+ hours per operator)  
- Certification program with re-testing every 6 months  
- Dual-operator verification for critical decisions (Level 3 and 4 escalations)  
- Post-incident review board for any operator intervention  
- Automated override if operator command contradicts safety rules (Layer 1\)  
- Clear escalation protocols with decision trees in operator dashboard  
- Regular drills: Unannounced simulation injects

Prototype Experiment  
Operator-in-the-Loop Simulation

* 10 operators complete 20 simulated mission each  
* Inject random faults: battery spike, signal loss, weather change, OTP timeout  
* Measure: response time, decision accuracy, stress indicators (heart rate optional)  
* Compare against automated fallback decisions

Validation Criteria

* \<5% operator error rate in simulation (wrong abort, wrong continue)  
* 100% compliance with safety hierarchy (no Layer 1 overrides)  
* Response times within timeouts: Level 3 \<2 min, Level 4 \<30 sec for 95% of cases  
* All operators certified before first physical flight

Owner: Training Lead  
Due Date: Before Phase 2 start

RISK 8 \- External System Overload/Abuse 

| Attribute | Value |
| :---- | :---- |
| Risk ID | R8 |
| Risk Name | External System Overload |
| Uncertainty | Can external partners send more requests than contracted? Will misconfigured webhooks flood ADOS? What if the external system goes down during an active mission? |
| Assumption | API quota system works; webhook delivery is reliable |
| No Proof Yet | System behavior under 10x quota; mission continuation during external outage |
| Likelihood | 2 (Unlikely \- but possible with growth) |
| Impact | 3 (Medium \- degradation) |
| Risk Score | 6 |
| Priority | MEDIUM |

Mitigation Strategy

- Implement API rate limiting per business  
- Dead letter queue for failed webhooks (retry with exponential backoff)  
- Circuit breaker pattern for external calls (fail fast, degrade gracefully)  
- Mission continuation if external system unreachable (autonomous fallback for up to 15 min)  
- Business quarantine: auto-block if quota exceeded repeatedly  
- Monitor external response times and failure rates

Prototype Experiment  
Load Test & Failure Simulation

* Generate 10x quota limit bursts from simulated business  
* Simulate external system down during active mission (at pickup, en route, at delivery)  
* Measure: system degradation, queue depth, mission success rate

Validation Criteria

* No system degradation under 2x quota  
* Graceful rate limiting at quota boundary (HTTP 429 with retry-after)  
* Missions complete even if external unreachable for up to 5 minutes  
* Failed webhooks successfully retried within 1 hour  
* Circuit breaker trips after 5 consecutive failures

Owner: Platform Engineer  
Due Date: Before API launch (Phase 2\)

RISK 9 \- Data Breach/ PII Exposure 

| Attribute | Value |
| :---- | :---- |
| Risk ID | R9 |
| Risk Name | Data Breach |
| Uncertainty | Can encrypted PII be decrypted if keys are compromised? Are all data access points properly secured? What about third-party integrations |
| Assumption | Encryption is sufficient; access logs deter misuse |
| No Proof Yet | Penetration test results; breach detection time |
| Likelihood | 2 (Unlikely \- with proper controls) |
| Impact | 5 (Existential \- regulatory fines, loss of trust) |
| Risk Score | 10 |
| Priority | HIGH |

Mitigation Strategy

- Key rotation policy (every 90 days) with secure key management (HSM/vault)  
- Database encryption at rest (PostgreSQL TDE, S3 server-side)  
- PII fields encrypted at application level (not just database)  
- All PII fields masked in logs  
- Regular security audits (quarterly)  
- Breach notification protocol (within 24 hours to NCAA/NITDA)  
- Access logging for all PII views   
- Minimum privilege principle: operators see only data needed for current mission

Prototype Experiment  
Security Penetration Test

* Third-party security audit before Phase 2  
* Simulated breach attempt: measure detection time  
* Test: SQL injection, API abuse, unauthorized data access  
* Verify encryption at rest and in transit

Validation Criteria

* Zero PII in logs (automated scan)  
* All access logged and auditable  
* Detection time \<1 hour for simulated breach  
* Penetration time passes with no critical findings  
* Key rotated at least once before Phase 2

Owner: Security Officer  
Due Date: Continuous \- quarterly audits

RISK 10 \- OTP Verification Timeout Cascades

| Attribute | Value |
| :---- | :---- |
| Risk ID | R10 |
| Risk Name | OTP Timeout Cascade |
| Uncertainty | What if the recipient doesn't respond within timeout? Drone returns with package \- customer impact? Multiple timeouts could strand drones away from base |
| Assumption | 5-minute timeout is sufficient; return-to-pickup is acceptable fallback |
| No Proof Yet | Actual response times in Abuja; customer satisfaction with timeouts |
| Likelihood | 3 (Possible \- real-world variability) |
| Impact | 2 (Low \- customer experience) |
| Risk Score | 6 |
| Priority | MEDIUM |

Mitigation Strategy

- Extend timeout dynamically based on context (urban 5 min, rural 8 min)  
- Allow operator to extend timeout remotely (via dashboard)  
- Pre-position backup drones near high-failure areas (optional)  
- Customer notification: SMS at arrival, reminder at 3 min, final warning at 4 min  
- Analyze failure patterns to identify problematic zones of times  
- Return-to-pickup vs return-to-warehouse decision configurable per business

Prototype Experiment  
Response Time Measurement

* Track actual response times in first 100 deliveries  
* Analyze by: time of day, location, contact method (phone vs SMS vs WhatsApp)  
* Survey customers: satisfaction with timeout duration  
* Test different timeout values: 3 min, 5 min, 8 min

Validation Criteria

* \<10% timeout rate (missions where no response)  
* Customer satisfaction \>90% even when timeout occurs (clear communication)  
* Return-to-pickup successful in 100% of timeout cases  
* No safety incidents related to hovering during timeout  
* Timeout config updated based on real data within first month

Owner: Product Manager  
Due Date: During Phase 2

4. Risk Quantification Matrix

| Risk ID | Risk Name | Likelihood | Impact | Risk Score | Priority |
| :---- | :---- | :---- | :---- | :---- | :---- |
| R1 | Battery Model Error | 4 | 5 | 20 | CRITICAL |
| R2 | Regulatory Restrictions | 3 | 5 | 15 | CRITICAL |
| R3 | Cellular Instability | 4 | 4 | 16 | CRITICAL |
| R4 | Reroute Latency | 3 | 4 | 12 | HIGH |
| R5 | Container Mechanical | 2 | 3 | 6 | MEDIUM |
| R6 | Visual ID (Phase 3\) | 1 | 3 | 3 | LOW |
| R7 | Operator Error | 3 | 4 | 12 | HIGH |
| R8 | External System Overload | 2 | 3 | 6 | MEDIUM |
| R9 | Data Breach | 2 | 5 | 10 | HIGH |
| R10 | OTP Timeout Cascade | 3 | 2 | 6 | MEDIUM |

Risk Thresholds:

* 15-25: CRITICAL \- MUST mitigate before Phase 2  
* 10-14: HIGH \- Active monitoring required, mitigation in place  
* 5-9: MEDIUM \- Standard mitigation, accept with monitoring  
* 1-4: LOW \- Accept/Watch, re-evaluate quarterly

5. RISK Ownership & Timeline

| Risk ID | Owner | Mitigation Due | Review Frequency |
| :---- | :---- | :---- | :---- |
| R1 | Battery Engineer | Before Phase 2 start | Weekly during testing |
| R2 | Regulatory Lead | Ongoing \- update monthly | Monthly |
| R3 | Comms Engineer | Before Phase 2 start | Per test flight |
| R4 | Autonomy Lead | Before Phase 2 start | Per simulation run |
| R5 | Hardware Lead | Before Phase 2 start | Per 100 cycles |
| R6 | Product Manager | Re-evaluate Phase 3 | Quarterly |
| R7 | Training Lead | Before Phase 2 start | Per operator certification |
| R8 | Platform Engineer | Before API launch (Phase 2\) | Weekly monitoring |
| R9 | Security Officer | Continuous | Quarterly audit |
| R10 | Product Manager | During Phase 2 | Per mission review |

6. Risk Acceptance Criteria

A risk may be accepted (not fully mitigated) if:

- Impact is low (\<3 on 1-5 scale) AND likelihood is low (\<3)  
- Mitigation cost exceeds potential loss (explicit business decision required)  
- Temporary exposure with planned fix in next phase (documented in evolution plan)

Accepted Risks for Phase 1/2:

| Risk | Justification | Review Date |
| :---- | :---- | :---- |
| R6 (Visual ID) | Explicitly deferred to Phase 3; Phase 1 uses audio+OTP only | Quarterly |
| R5 partial (long-term durability) | Cannot fully test 1000 cycles before Phase 2; monitor in field | Per 100 cycles |

Never Accept: 

* Any risk with safety impact (R1, R3, R4 if they cause crashes)  
* Regulatory non-compliance (R2)  
* Data breach (R9)  
* Operator error without training (R7)

7. Risk Monitoring Cadence

| Cadence | Activity |
| :---- | :---- |
| Daily | Automated monitoring of telemetry for anomalies (R1, R3, R4); API quota usage (R8) |
| Weekly | Risk review meeting for active Phase 2 risks; update likelihood scores based on data |
| Monthly | Full risk register review; regulatory update (R2); security log review (R8) |
| Quarterly | External Security audit (R9); operator recertification (R7); Phase 3 re-evaluation (R6) |
| Per Milestone | Re-evaluate before Phase 2, Phase 3, Phase 4 transitions |

8. Incident Response Framework

If a risk materializes:

Phase 1: Immediate Response (First 1 Hour)

- Safety first \- Ground affected drones immediately  
- Contain \- Stop any ongoing similar operations  
- Notify \- Within 1 hour to: Risk Owner, Head of Engineering, Safety Officer  
- Document \- Capture all telemetry, logs, operator actions

Phase 2: Investigation (24-72 Hours)

- Root cause analysis \- Led by Risk Owner  
- Impact assessment \- How many missions are affected? Any injuries? Regulatory implications?  
- Fix identification \- What change prevents recurrence?

Phase 3: Resolution (Within 1 Week)

- Implement fix \- Code change, process update, training reinforcement  
- Verify \- Test fix simulation  
- Update risk register \- Adjust likelihood, add new controls

Phase 4: Communication (As Appropriate)

- Internal \- All operators briefed  
- Regulatory \- NCAA/NITDA if required by Part 18  
- Customer \- if delivery failure or data breach

Incident Severity Levels:

| Level | Description | Notification |
| :---- | :---- | :---- |
| 4 \- Critical | Emergency landing, injury, breach of PII | Immediate: CEO, NCAA within 24h |
| 3 \- High | Mission abort, cargo loss, extended downtime | Within 4 hours: Engineering lead |
| 2 \- Medium | Reroute, delay, customer complaint | Within 24 hours: Team lead |
| 1 \- Low | Minor deviation, no impact | Logged in post-mission review |

9. Connection to Validation Strategy

Each risk maps to validation tests defined in Autonomy Definition Section 16 and Data Architecture Section 22:

| Risk | Validation Test | Success Criteria |
| :---- | :---- | :---- |
| R1 | Battery anomaly injection; 1000 simulated missions | Error \< 10%; no voltage collapse |
| R2 | Regulatory sandbox test; geofence monitoring  | Zero violations; NCAA clearance |
| R3 | Signal loss simulation; cellular mapping | Reconnect \<10s; packet loss \<2% |
| R4 | Reroute stress scenarios; latency simulation | 95% \<500ms; concurrent storm \<2s |
| R5 | Weight sensor simulation; 1000 cycle test | Failure rate \<1%; drift \<100g |
| R6 | (Phase 3\) CV pipeline test | Confidence \> 0.85 for 90% |
| R7 | Operator-in-the-loop simulation | Error rate \< 5%; response within timeout |
| R8 | Load test; external failure simulation | Graceful degradation; mission completion |
| R9 | Penetration test; access log audit | Zero PII in logs; detection\<1h |
| R10 | Response time measurement; timeout analysis | Timeout rate \<10% |

10. Risk Register Maintenance

This document is a living artifact and must be:

* Updated monthly \- Review likelihood scores based on new data  
* Version controlled \- Track risk evolution over time  
* Reviewed before each phase gate \- Phase 1→2, 2→3, etc  
* Input to architecture decisions \- if risk is too high, change design  
* Accessible to all team members \- Transparency on what we don’ know

11. Glossary

| Term | Definition |
| :---- | :---- |
| AGL | Above Ground Level |
| BVLOS | Beyond Visual Line of Sight |
| CV | Computer Vision |
| DLQ | Dead Letter Queue |
| NCAA | Nigerian Civil Aviation Authority |
| NEMA | National Emergency Management Agency |
| NiMet | Nigerian Meteorological Agency |
| NITDA | National Information Technology Development Agency |
| OTP | One-Time Password |
| PII | Personally Identifiable Information |
| RTH | Return to Home |
| TDE | Transparent Data Encryption |

