"""[Observations.r](https://github.com/edwardlib/observations) provides
a one line Python API for loading standard data sets in machine
learning. It automates the process from downloading, extracting,
loading, and preprocessing data. Observations helps keep the workflow
reproducible and follow sensible standards.

Observations is a standalone Python library and must be installed
separate from Edward.
"""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from observations.r.air_passengers import air_passengers
from observations.r.bj_sales import bj_sales
from observations.r.bod import bod
from observations.r.co2 import co2
from observations.r.formaldehyde import formaldehyde
from observations.r.hair_eye_color import hair_eye_color
from observations.r.insect_sprays import insect_sprays
from observations.r.johnson_johnson import johnson_johnson
from observations.r.lake_huron import lake_huron
from observations.r.life_cycle_savings import life_cycle_savings
from observations.r.nile import nile
from observations.r.orchard_sprays import orchard_sprays
from observations.r.plant_growth import plant_growth
from observations.r.puromycin import puromycin
from observations.r.titanic import titanic
from observations.r.tooth_growth import tooth_growth
from observations.r.ucb_admissions import ucb_admissions
from observations.r.uk_driver_deaths import uk_driver_deaths
from observations.r.uk_gas import uk_gas
from observations.r.us_acc_deaths import us_acc_deaths
from observations.r.us_arrests import us_arrests
from observations.r.us_judge_ratings import us_judge_ratings
from observations.r.us_personal_expend import us_personal_expend
from observations.r.va_deaths import va_deaths
from observations.r.www_usage import www_usage
from observations.r.world_phones import world_phones
from observations.r.airmiles import airmiles
from observations.r.airquality import airquality
from observations.r.anscombe import anscombe
from observations.r.attenu import attenu
from observations.r.attitude import attitude
from observations.r.austres import austres
from observations.r.cars import cars
from observations.r.chickwts import chickwts
from observations.r.co2_1 import co2_1
from observations.r.crimtab import crimtab
from observations.r.discoveries import discoveries
from observations.r.esoph import esoph
from observations.r.euro import euro
from observations.r.faithful import faithful
from observations.r.freeny import freeny
from observations.r.infert import infert
from observations.r.iris import iris
from observations.r.islands import islands
from observations.r.lh import lh
from observations.r.longley import longley
from observations.r.lynx import lynx
from observations.r.morley import morley
from observations.r.mtcars import mtcars
from observations.r.nhtemp import nhtemp
from observations.r.nottem import nottem
from observations.r.npk import npk
from observations.r.occupational_status import occupational_status
from observations.r.precip import precip
from observations.r.presidents import presidents
from observations.r.pressure import pressure
from observations.r.quakes import quakes
from observations.r.randu import randu
from observations.r.rivers import rivers
from observations.r.rock import rock
from observations.r.sleep import sleep
from observations.r.stackloss import stackloss
from observations.r.sunspot_month import sunspot_month
from observations.r.sunspot_year import sunspot_year
from observations.r.sunspots import sunspots
from observations.r.swiss import swiss
from observations.r.treering import treering
from observations.r.trees import trees
from observations.r.uspop import uspop
from observations.r.volcano import volcano
from observations.r.warpbreaks import warpbreaks
from observations.r.women import women
from observations.r.acme import acme
from observations.r.aids import aids
from observations.r.aircondit import aircondit
from observations.r.aircondit7 import aircondit7
from observations.r.amis import amis
from observations.r.aml import aml
from observations.r.bigcity import bigcity
from observations.r.brambles import brambles
from observations.r.breslow import breslow
from observations.r.calcium import calcium
from observations.r.cane import cane
from observations.r.capability import capability
from observations.r.cats_m import cats_m
from observations.r.cav import cav
from observations.r.cd4 import cd4
from observations.r.channing import channing
from observations.r.city import city
from observations.r.claridge import claridge
from observations.r.cloth import cloth
from observations.r.co_transfer import co_transfer
from observations.r.coal import coal
from observations.r.darwin import darwin
from observations.r.dogs import dogs
from observations.r.downs_bc import downs_bc
from observations.r.ducks import ducks
from observations.r.fir import fir
from observations.r.frets import frets
from observations.r.grav import grav
from observations.r.gravity import gravity
from observations.r.hirose import hirose
from observations.r.islay import islay
from observations.r.manaus import manaus
from observations.r.melanoma import melanoma
from observations.r.motor import motor
from observations.r.neuro import neuro
from observations.r.nitrofen import nitrofen
from observations.r.nodal import nodal
from observations.r.nuclear import nuclear
from observations.r.paulsen import paulsen
from observations.r.poisons import poisons
from observations.r.polar import polar
from observations.r.remission import remission
from observations.r.salinity import salinity
from observations.r.survival import survival
from observations.r.tau import tau
from observations.r.tuna import tuna
from observations.r.urine import urine
from observations.r.wool import wool
from observations.r.acf1 import acf1
from observations.r.cars93_summary import cars93_summary
from observations.r.lottario import lottario
from observations.r.manitoba_lakes import manitoba_lakes
from observations.r.sp500_w90 import sp500_w90
from observations.r.sp500_close import sp500_close
from observations.r.ais import ais
from observations.r.allbacks import allbacks
from observations.r.anesthetic import anesthetic
from observations.r.ant111b import ant111b
from observations.r.antigua import antigua
from observations.r.appletaste import appletaste
from observations.r.aulatlong import aulatlong
from observations.r.austpop import austpop
from observations.r.biomass import biomass
from observations.r.bomregions import bomregions
from observations.r.bomregions2011 import bomregions2011
from observations.r.bomregions2012 import bomregions2012
from observations.r.bomsoi import bomsoi
from observations.r.bomsoi2001 import bomsoi2001
from observations.r.carprice import carprice
from observations.r.cerealsugar import cerealsugar
from observations.r.cfseal import cfseal
from observations.r.cities import cities
from observations.r.codling import codling
from observations.r.cottonworkers import cottonworkers
from observations.r.cps1 import cps1
from observations.r.cps2 import cps2
from observations.r.cps3 import cps3
from observations.r.cricketer import cricketer
from observations.r.cuckoohosts import cuckoohosts
from observations.r.cuckoos import cuckoos
from observations.r.dengue import dengue
from observations.r.dewpoint import dewpoint
from observations.r.droughts import droughts
from observations.r.edc_co2 import edc_co2
from observations.r.edc_t import edc_t
from observations.r.elastic1 import elastic1
from observations.r.elastic2 import elastic2
from observations.r.elasticband import elasticband
from observations.r.fossilfuel import fossilfuel
from observations.r.fossum import fossum
from observations.r.frogs import frogs
from observations.r.frostedflakes import frostedflakes
from observations.r.fruitohms import fruitohms
from observations.r.gaba import gaba
from observations.r.geophones import geophones
from observations.r.grog import grog
from observations.r.head_injury import head_injury
from observations.r.hills import hills
from observations.r.hills2000 import hills2000
from observations.r.hotspots import hotspots
from observations.r.hotspots2006 import hotspots2006
from observations.r.houseprices import houseprices
from observations.r.humanpower1 import humanpower1
from observations.r.humanpower2 import humanpower2
from observations.r.hurric_named import hurric_named
from observations.r.intersalt import intersalt
from observations.r.ironslag import ironslag
from observations.r.jobs import jobs
from observations.r.kiwishade import kiwishade
from observations.r.leafshape import leafshape
from observations.r.leafshape17 import leafshape17
from observations.r.leaftemp import leaftemp
from observations.r.leaftemp_all import leaftemp_all
from observations.r.litters import litters
from observations.r.lung import lung
from observations.r.measles import measles
from observations.r.med_expenses import med_expenses
from observations.r.mifem import mifem
from observations.r.mignonette import mignonette
from observations.r.milk import milk
from observations.r.modelcars import modelcars
from observations.r.monica import monica
from observations.r.moths import moths
from observations.r.nass_cds import nass_cds
from observations.r.nasshead import nasshead
from observations.r.nihills import nihills
from observations.r.nsw74demo import nsw74demo
from observations.r.nsw74psid1 import nsw74psid1
from observations.r.nsw74psid3 import nsw74psid3
from observations.r.nsw74psid_a import nsw74psid_a
from observations.r.nswdemo import nswdemo
from observations.r.nswpsid1 import nswpsid1
from observations.r.oddbooks import oddbooks
from observations.r.orings import orings
from observations.r.pair65 import pair65
from observations.r.possum import possum
from observations.r.possumsites import possumsites
from observations.r.primates import primates
from observations.r.progression import progression
from observations.r.psid1 import psid1
from observations.r.psid2 import psid2
from observations.r.psid3 import psid3
from observations.r.races2000 import races2000
from observations.r.rainforest import rainforest
from observations.r.rareplants import rareplants
from observations.r.rice import rice
from observations.r.rock_art import rock_art
from observations.r.roller import roller
from observations.r.science import science
from observations.r.seedrates import seedrates
from observations.r.socsupport import socsupport
from observations.r.softbacks import softbacks
from observations.r.sorption import sorption
from observations.r.spam7 import spam7
from observations.r.st_vincent import st_vincent
from observations.r.sugar import sugar
from observations.r.tinting import tinting
from observations.r.tomato import tomato
from observations.r.toycars import toycars
from observations.r.vince111b import vince111b
from observations.r.vlt import vlt
from observations.r.wages1833 import wages1833
from observations.r.world_records import world_records
from observations.r.fars import fars
from observations.r.air_accs import air_accs
from observations.r.cvalues import cvalues
from observations.r.fars2007 import fars2007
from observations.r.fars2008 import fars2008
from observations.r.german import german
from observations.r.loti import loti
from observations.r.alloauto import alloauto
from observations.r.allograft import allograft
from observations.r.azt import azt
from observations.r.baboon import baboon
from observations.r.bcdeter import bcdeter
from observations.r.bfeed import bfeed
from observations.r.bmt import bmt
from observations.r.bnct import bnct
from observations.r.btrial import btrial
from observations.r.burn import burn
from observations.r.drug6mp import drug6mp
from observations.r.drughiv import drughiv
from observations.r.hodg import hodg
from observations.r.kidrecurr import kidrecurr
from observations.r.kidtran import kidtran
from observations.r.larynx import larynx
from observations.r.pneumon import pneumon
from observations.r.psych import psych
from observations.r.std import std
from observations.r.stddiag import stddiag
from observations.r.tongue import tongue
from observations.r.twins import twins
from observations.r.animals2 import animals2
from observations.r.crohn_d import crohn_d
from observations.r.n_ox_emissions import n_ox_emissions
from observations.r.siegels_ex import siegels_ex
from observations.r.aircraft import aircraft
from observations.r.airmay import airmay
from observations.r.alcohol import alcohol
from observations.r.ambient_noxch import ambient_noxch
from observations.r.biomass_till import biomass_till
from observations.r.bushfire import bushfire
from observations.r.carrots import carrots
from observations.r.cloud import cloud
from observations.r.coleman import coleman
from observations.r.condroz import condroz
from observations.r.cushny import cushny
from observations.r.delivery import delivery
from observations.r.education import education
from observations.r.epilepsy import epilepsy
from observations.r.ex_am import ex_am
from observations.r.foodstamp import foodstamp
from observations.r.hbk import hbk
from observations.r.heart import heart
from observations.r.kootenay import kootenay
from observations.r.lactic import lactic
from observations.r.pension import pension
from observations.r.phosphor import phosphor
from observations.r.pilot import pilot
from observations.r.possum_div import possum_div
from observations.r.pulpfiber import pulpfiber
from observations.r.radar_image import radar_image
from observations.r.stars_cyg import stars_cyg
from observations.r.telef import telef
from observations.r.toxicity import toxicity
from observations.r.vaso import vaso
from observations.r.wagner_growth import wagner_growth
from observations.r.wood import wood
from observations.r.ams_survey import ams_survey
from observations.r.adler import adler
from observations.r.angell import angell
from observations.r.us_public_school import us_public_school
from observations.r.baumann import baumann
from observations.r.bfox import bfox
from observations.r.blackmore import blackmore
from observations.r.burt import burt
from observations.r.can_pop import can_pop
from observations.r.chile import chile
from observations.r.chirot import chirot
from observations.r.cowles import cowles
from observations.r.davis import davis
from observations.r.davis_thin import davis_thin
from observations.r.depredations import depredations
from observations.r.duncan import duncan
from observations.r.ericksen import ericksen
from observations.r.florida import florida
from observations.r.freedman import freedman
from observations.r.friendly import friendly
from observations.r.ginzberg import ginzberg
from observations.r.greene import greene
from observations.r.guyer import guyer
from observations.r.hartnagel import hartnagel
from observations.r.highway1 import highway1
from observations.r.kostecki_dillon import kostecki_dillon
from observations.r.leinhardt import leinhardt
from observations.r.lo_bd import lo_bd
from observations.r.mandel import mandel
from observations.r.migration import migration
from observations.r.moore import moore
from observations.r.mroz import mroz
from observations.r.o_brien_kaiser import o_brien_kaiser
from observations.r.ornstein import ornstein
from observations.r.pottery import pottery
from observations.r.prestige import prestige
from observations.r.quartet import quartet
from observations.r.robey import robey
from observations.r.slid import slid
from observations.r.sahlins import sahlins
from observations.r.salaries import salaries
from observations.r.soils import soils
from observations.r.states import states
from observations.r.transact import transact
from observations.r.gdp_infant_mortality import gdp_infant_mortality
from observations.r.us_pop import us_pop
from observations.r.vocab import vocab
from observations.r.weight_loss import weight_loss
from observations.r.womenlf import womenlf
from observations.r.wong import wong
from observations.r.wool1 import wool1
from observations.r.agriculture import agriculture
from observations.r.animals import animals
from observations.r.chor_sub import chor_sub
from observations.r.flower import flower
from observations.r.plant_traits import plant_traits
from observations.r.pluton import pluton
from observations.r.ruspini import ruspini
from observations.r.votes_repub import votes_repub
from observations.r.xclara import xclara
from observations.r.affairs import affairs
from observations.r.azcabgptca import azcabgptca
from observations.r.azdrg112 import azdrg112
from observations.r.azpro import azpro
from observations.r.azprocedure import azprocedure
from observations.r.badhealth import badhealth
from observations.r.fasttrakg import fasttrakg
from observations.r.fishing import fishing
from observations.r.lbw import lbw
from observations.r.lbwgrp import lbwgrp
from observations.r.loomis import loomis
from observations.r.mdvis import mdvis
from observations.r.medpar import medpar
from observations.r.nuts import nuts
from observations.r.rwm import rwm
from observations.r.rwm1984 import rwm1984
from observations.r.rwm5yr import rwm5yr
from observations.r.smoking import smoking
from observations.r.titanicgrp import titanicgrp
from observations.r.accident import accident
from observations.r.airline import airline
from observations.r.airq import airq
from observations.r.benefits import benefits
from observations.r.bids import bids
from observations.r.budget_food import budget_food
from observations.r.budget_italy import budget_italy
from observations.r.budget_uk import budget_uk
from observations.r.bwages import bwages
from observations.r.cp_sch3 import cp_sch3
from observations.r.cran_packages import cran_packages
from observations.r.capm import capm
from observations.r.car import car
from observations.r.caschool import caschool
from observations.r.catsup import catsup
from observations.r.cigar import cigar
from observations.r.cigarette import cigarette
from observations.r.clothing import clothing
from observations.r.computers import computers
from observations.r.cracker import cracker
from observations.r.crime import crime
from observations.r.dm import dm
from observations.r.diamond import diamond
from observations.r.doctor import doctor
from observations.r.doctor_aus import doctor_aus
from observations.r.doctor_contacts import doctor_contacts
from observations.r.earnings import earnings
from observations.r.electricity import electricity
from observations.r.fair import fair
from observations.r.fatality import fatality
from observations.r.fishing1 import fishing1
from observations.r.forward import forward
from observations.r.friend_foe import friend_foe
from observations.r.garch import garch
from observations.r.gasoline import gasoline
from observations.r.griliches import griliches
from observations.r.grunfeld import grunfeld
from observations.r.hc_choice_california import hc_choice_california
from observations.r.hhs_cybsec_breaches import hhs_cybsec_breaches
from observations.r.hi_hours_worked import hi_hours_worked
from observations.r.hdma import hdma
from observations.r.heating import heating
from observations.r.hedonic import hedonic
from observations.r.hmda import hmda
from observations.r.housing import housing
from observations.r.icecream import icecream
from observations.r.journals import journals
from observations.r.kakadu import kakadu
from observations.r.ketchup import ketchup
from observations.r.klein import klein
from observations.r.labor_supply import labor_supply
from observations.r.labour import labour
from observations.r.mcas import mcas
from observations.r.males import males
from observations.r.mathlevel import mathlevel
from observations.r.med_exp import med_exp
from observations.r.metal import metal
from observations.r.mode import mode
from observations.r.mode_choice import mode_choice
from observations.r.mofa import mofa
from observations.r.mroz1 import mroz1
from observations.r.mun_exp import mun_exp
from observations.r.natural_park import natural_park
from observations.r.nerlove import nerlove
from observations.r.ofp import ofp
from observations.r.oil import oil
from observations.r.psid import psid
from observations.r.participation import participation
from observations.r.patents_hgh import patents_hgh
from observations.r.patents_rd import patents_rd
from observations.r.pound import pound
from observations.r.produc import produc
from observations.r.ret_school import ret_school
from observations.r.sp500 import sp500
from observations.r.schooling import schooling
from observations.r.somerville import somerville
from observations.r.star import star
from observations.r.strike import strike
from observations.r.strike_dur import strike_dur
from observations.r.strike_nb import strike_nb
from observations.r.tobacco import tobacco
from observations.r.train import train
from observations.r.transp_eq import transp_eq
from observations.r.treatment import treatment
from observations.r.tuna1 import tuna1
from observations.r.us_finance_industry import us_finance_industry
from observations.r.us_gdp_presidents import us_gdp_presidents
from observations.r.us_classified_docs import us_classified_docs
from observations.r.us_state_abbrev import us_state_abbrev
from observations.r.us_tax_words import us_tax_words
from observations.r.unemp_dur import unemp_dur
from observations.r.unemployment import unemployment
from observations.r.university import university
from observations.r.vietnam_h import vietnam_h
from observations.r.vietnam_i import vietnam_i
from observations.r.wages import wages
from observations.r.wages1 import wages1
from observations.r.workinghours import workinghours
from observations.r.yen import yen
from observations.r.yogurt import yogurt
from observations.r.banking_crises import banking_crises
from observations.r.breaches import breaches
from observations.r.terr_incidents import terr_incidents
from observations.r.income_inequality import income_inequality
from observations.r.nkill_by_country_yr import nkill_by_country_yr
from observations.r.non_english_names import non_english_names
from observations.r.political_knowledge import political_knowledge
from observations.r.terrorism import terrorism
from observations.r.parkinsons import parkinsons
from observations.r.aldh2 import aldh2
from observations.r.apoeapoc import apoeapoc
from observations.r.cf import cf
from observations.r.crohn import crohn
from observations.r.fa import fa
from observations.r.fsnps import fsnps
from observations.r.hla import hla
from observations.r.hr1420 import hr1420
from observations.r.l51 import l51
from observations.r.lukas import lukas
from observations.r.mao import mao
from observations.r.meyer import meyer
from observations.r.mfblong import mfblong
from observations.r.mhtdata import mhtdata
from observations.r.nep499 import nep499
from observations.r.luv_colours import luv_colours
from observations.r.arbuthnot import arbuthnot
from observations.r.armada import armada
from observations.r.bowley import bowley
from observations.r.cavendish import cavendish
from observations.r.chest_sizes import chest_sizes
from observations.r.cholera import cholera
from observations.r.cushny_peebles import cushny_peebles
from observations.r.cushny_peebles_n import cushny_peebles_n
from observations.r.dactyl import dactyl
from observations.r.drinks_wages import drinks_wages
from observations.r.fingerprints import fingerprints
from observations.r.galton import galton
from observations.r.galton_families import galton_families
from observations.r.guerry import guerry
from observations.r.halley_life_table import halley_life_table
from observations.r.jevons import jevons
from observations.r.langren_all import langren_all
from observations.r.langren1644 import langren1644
from observations.r.macdonell import macdonell
from observations.r.macdonell_df import macdonell_df
from observations.r.michelson import michelson
from observations.r.michelson_sets import michelson_sets
from observations.r.minard_cities import minard_cities
from observations.r.minard_temp import minard_temp
from observations.r.minard_troops import minard_troops
from observations.r.nightingale import nightingale
from observations.r.old_maps import old_maps
from observations.r.pearson_lee import pearson_lee
from observations.r.polio_trials import polio_trials
from observations.r.prostitutes import prostitutes
from observations.r.pyx import pyx
from observations.r.quarrels import quarrels
from observations.r.snow_dates import snow_dates
from observations.r.snow_deaths import snow_deaths
from observations.r.snow_deaths2 import snow_deaths2
from observations.r.snow_pumps import snow_pumps
from observations.r.snow_streets import snow_streets
from observations.r.wheat import wheat
from observations.r.wheat_monarchs import wheat_monarchs
from observations.r.yeast import yeast
from observations.r.yeast_d_mat import yeast_d_mat
from observations.r.zea_mays import zea_mays
from observations.r.barley import barley
from observations.r.environmental import environmental
from observations.r.ethanol import ethanol
from observations.r.melanoma import melanoma
from observations.r.singer import singer
from observations.r.aids2 import aids2
from observations.r.animals1 import animals1
from observations.r.boston import boston
from observations.r.cars93 import cars93
from observations.r.cushings import cushings
from observations.r.ddt_kale import ddt_kale
from observations.r.gag_urine import gag_urine
from observations.r.insurance import insurance
from observations.r.melanoma1 import melanoma1
from observations.r.ome_children import ome_children
from observations.r.pima_te import pima_te
from observations.r.pima_tr import pima_tr
from observations.r.pima_tr2 import pima_tr2
from observations.r.rabbit import rabbit
from observations.r.rubber import rubber
from observations.r.sitka import sitka
from observations.r.sitka89 import sitka89
from observations.r.skye import skye
from observations.r.traffic import traffic
from observations.r.us_cereal import us_cereal
from observations.r.us_crime import us_crime
from observations.r.va_lung_cancer import va_lung_cancer
from observations.r.abbey import abbey
from observations.r.accdeaths import accdeaths
from observations.r.anorexia import anorexia
from observations.r.bacteria import bacteria
from observations.r.beav1 import beav1
from observations.r.beav2 import beav2
from observations.r.biopsy import biopsy
from observations.r.birthwt import birthwt
from observations.r.cabbages import cabbages
from observations.r.caith import caith
from observations.r.cats import cats
from observations.r.cement import cement
from observations.r.chem import chem
from observations.r.coop import coop
from observations.r.cpus import cpus
from observations.r.crabs import crabs
from observations.r.deaths import deaths
from observations.r.drivers import drivers
from observations.r.eagles import eagles
from observations.r.epil import epil
from observations.r.farms import farms
from observations.r.fgl import fgl
from observations.r.forbes import forbes
from observations.r.galaxies import galaxies
from observations.r.gehan import gehan
from observations.r.genotype import genotype
from observations.r.geyser import geyser
from observations.r.gilgais import gilgais
from observations.r.housing1 import housing1
from observations.r.immer import immer
from observations.r.leuk import leuk
from observations.r.mammals import mammals
from observations.r.mcycle import mcycle
from observations.r.menarche import menarche
from observations.r.michelson1 import michelson1
from observations.r.minn38 import minn38
from observations.r.motors import motors
from observations.r.muscle import muscle
from observations.r.newcomb import newcomb
from observations.r.nlschools import nlschools
from observations.r.npr1 import npr1
from observations.r.oats import oats
from observations.r.painters import painters
from observations.r.petrol import petrol
from observations.r.quine import quine
from observations.r.road import road
from observations.r.rotifer import rotifer
from observations.r.ships import ships
from observations.r.shrimp import shrimp
from observations.r.shuttle import shuttle
from observations.r.snails import snails
from observations.r.steam import steam
from observations.r.stormer import stormer
from observations.r.survey import survey
from observations.r.synth_te import synth_te
from observations.r.synth_tr import synth_tr
from observations.r.topo import topo
from observations.r.waders import waders
from observations.r.whiteside import whiteside
from observations.r.wtloss import wtloss
from observations.r.empl_uk import empl_uk
from observations.r.grunfeld1 import grunfeld1
from observations.r.males1 import males1
from observations.r.parity import parity
from observations.r.rice_farms import rice_farms
from observations.r.snmesp import snmesp
from observations.r.sum_hes import sum_hes
from observations.r.baseball import baseball
from observations.r.aus_election_polling import aus_election_polling
from observations.r.australian_elections import australian_elections
from observations.r.efron_morris import efron_morris
from observations.r.rock_the_vote import rock_the_vote
from observations.r.uk_house_of_commons import uk_house_of_commons
from observations.r.absentee import absentee
from observations.r.admit import admit
from observations.r.bio_chemists import bio_chemists
from observations.r.ca2006 import ca2006
from observations.r.iraq_vote import iraq_vote
from observations.r.political_info import political_info
from observations.r.president_elections import president_elections
from observations.r.prussian import prussian
from observations.r.union_density import union_density
from observations.r.vote92 import vote92
from observations.r.french_fries import french_fries
from observations.r.tips import tips
from observations.r.car_test_frame import car_test_frame
from observations.r.car90 import car90
from observations.r.cu_summary import cu_summary
from observations.r.kyphosis import kyphosis
from observations.r.solder import solder
from observations.r.stagec import stagec
from observations.r.public_schools import public_schools
from observations.r.bollen import bollen
from observations.r.cnes import cnes
from observations.r.klein1 import klein1
from observations.r.mental_tests import mental_tests
from observations.r.bladder import bladder
from observations.r.cancer import cancer
from observations.r.cgd import cgd
from observations.r.colon import colon
from observations.r.flchain import flchain
from observations.r.genfan import genfan
from observations.r.kidney import kidney
from observations.r.leukemia import leukemia
from observations.r.logan import logan
from observations.r.lung import lung
from observations.r.mgus import mgus
from observations.r.mgus2 import mgus2
from observations.r.myeloid import myeloid
from observations.r.nwtco import nwtco
from observations.r.ovarian import ovarian
from observations.r.pbc import pbc
from observations.r.rats import rats
from observations.r.retinopathy import retinopathy
from observations.r.rh_dnase import rh_dnase
from observations.r.stanford2 import stanford2
from observations.r.tobin import tobin
from observations.r.transplant import transplant
from observations.r.veteran import veteran
from observations.r.arthritis import arthritis
from observations.r.baseball1 import baseball1
from observations.r.broken_marriage import broken_marriage
from observations.r.bundesliga import bundesliga
from observations.r.bundestag2005 import bundestag2005
from observations.r.butterfly import butterfly
from observations.r.coal_miners import coal_miners
from observations.r.danish_welfare import danish_welfare
from observations.r.employment import employment
from observations.r.federalist import federalist
from observations.r.hitters import hitters
from observations.r.horse_kicks import horse_kicks
from observations.r.hospital import hospital
from observations.r.job_satisfaction import job_satisfaction
from observations.r.joint_sports import joint_sports
from observations.r.lifeboats import lifeboats
from observations.r.non_response import non_response
from observations.r.ovary_cancer import ovary_cancer
from observations.r.pre_sex import pre_sex
from observations.r.punishment import punishment
from observations.r.rep_vict import rep_vict
from observations.r.saxony import saxony
from observations.r.sexual_fun import sexual_fun
from observations.r.space_shuttle import space_shuttle
from observations.r.suicide import suicide
from observations.r.trucks import trucks
from observations.r.uk_soccer import uk_soccer
from observations.r.visual_acuity import visual_acuity
from observations.r.von_bort import von_bort
from observations.r.weldon_dice import weldon_dice
from observations.r.women_queue import women_queue
from observations.r.p_erisk import p_erisk
from observations.r.supreme_court import supreme_court
from observations.r.weimar import weimar
from observations.r.approval import approval
from observations.r.bivariate import bivariate
from observations.r.coalition import coalition
from observations.r.coalition2 import coalition2
from observations.r.eidat import eidat
from observations.r.free1 import free1
from observations.r.free2 import free2
from observations.r.friendship import friendship
from observations.r.grunfeld2 import grunfeld2
from observations.r.hoff import hoff
from observations.r.homerun import homerun
from observations.r.immi1 import immi1
from observations.r.immi2 import immi2
from observations.r.immi3 import immi3
from observations.r.immi4 import immi4
from observations.r.immi5 import immi5
from observations.r.immigration import immigration
from observations.r.klein2 import klein2
from observations.r.kmenta2 import kmenta2
from observations.r.macro import macro
from observations.r.mexico import mexico
from observations.r.mid import mid
from observations.r.newpainters import newpainters
from observations.r.sanction import sanction
from observations.r.seatshare import seatshare
from observations.r.sna_ex import sna_ex
from observations.r.turnout import turnout
from observations.r.voteincome import voteincome
from observations.r.bcg_vaccine import bcg_vaccine
from observations.r.bthe_b import bthe_b
from observations.r.cygob1 import cygob1
from observations.r.forbes2000 import forbes2000
from observations.r.ghq import ghq
from observations.r.lanza import lanza
from observations.r.agefat import agefat
from observations.r.aspirin import aspirin
from observations.r.birthdeathrates import birthdeathrates
from observations.r.bladdercancer import bladdercancer
from observations.r.clouds import clouds
from observations.r.foster import foster
from observations.r.heptathlon import heptathlon
from observations.r.mastectomy import mastectomy
from observations.r.meteo import meteo
from observations.r.orallesions import orallesions
from observations.r.phosphate import phosphate
from observations.r.pistonrings import pistonrings
from observations.r.planets import planets
from observations.r.plasma import plasma
from observations.r.polyps import polyps
from observations.r.polyps3 import polyps3
from observations.r.pottery1 import pottery1
from observations.r.rearrests import rearrests
from observations.r.respiratory import respiratory
from observations.r.roomwidth import roomwidth
from observations.r.schizophrenia import schizophrenia
from observations.r.schizophrenia2 import schizophrenia2
from observations.r.schooldays import schooldays
from observations.r.skulls import skulls
from observations.r.students import students
from observations.r.suicides import suicides
from observations.r.toothpaste import toothpaste
from observations.r.voting import voting
from observations.r.water import water
from observations.r.watervoles import watervoles
from observations.r.waves import waves
from observations.r.weightgain import weightgain
from observations.r.womensrole import womensrole
from observations.r.bechtoldt import bechtoldt
from observations.r.bechtoldt_1 import bechtoldt_1
from observations.r.bechtoldt_2 import bechtoldt_2
from observations.r.dwyer import dwyer
from observations.r.gleser import gleser
from observations.r.gorsuch import gorsuch
from observations.r.harman_5 import harman_5
from observations.r.harman_8 import harman_8
from observations.r.harman_political import harman_political
from observations.r.holzinger import holzinger
from observations.r.holzinger_9 import holzinger_9
from observations.r.reise import reise
from observations.r.schmid import schmid
from observations.r.schutz import schutz
from observations.r.thurstone import thurstone
from observations.r.thurstone_33 import thurstone_33
from observations.r.tucker import tucker
from observations.r.ability import ability
from observations.r.affect import affect
from observations.r.bfi import bfi
from observations.r.bfi_dictionary import bfi_dictionary
from observations.r.blot import blot
from observations.r.burt1 import burt1
from observations.r.cattell import cattell
from observations.r.cities1 import cities1
from observations.r.cubits import cubits
from observations.r.epi import epi
from observations.r.epi_bfi import epi_bfi
from observations.r.epi_dictionary import epi_dictionary
from observations.r.galton1 import galton1
from observations.r.heights import heights
from observations.r.income import income
from observations.r.iqitems import iqitems
from observations.r.msq import msq
from observations.r.neo import neo
from observations.r.peas import peas
from observations.r.sat_act import sat_act
from observations.r.within_between import within_between
from observations.r.bosco import bosco
from observations.r.cobar_ore import cobar_ore
from observations.r.mammals1 import mammals1
from observations.r.barro import barro
from observations.r.engel import engel
from observations.r.gasprice import gasprice
from observations.r.uis import uis
from observations.r.dietox import dietox
from observations.r.koch import koch
from observations.r.ohio import ohio
from observations.r.respdis import respdis
from observations.r.seizure import seizure
from observations.r.spruce import spruce
from observations.r.liver import liver
from observations.r.nidd import nidd
from observations.r.portpirie import portpirie
from observations.r.rain import rain
from observations.r.summer import summer
from observations.r.wavesurge import wavesurge
from observations.r.winter import winter
from observations.r.arthritis1 import arthritis1
from observations.r.bmw import bmw
from observations.r.danish import danish
from observations.r.nidd_annual import nidd_annual
from observations.r.nidd_thresh import nidd_thresh
from observations.r.siemens import siemens
from observations.r.sp_raw import sp_raw
from observations.r.spto87 import spto87
from observations.r.arabidopsis import arabidopsis
from observations.r.dyestuff import dyestuff
from observations.r.dyestuff2 import dyestuff2
from observations.r.pastes import pastes
from observations.r.penicillin import penicillin
from observations.r.verb_agg import verb_agg
from observations.r.cake import cake
from observations.r.cbpp import cbpp
from observations.r.grouseticks import grouseticks
from observations.r.sleepstudy import sleepstudy
from observations.r.alcohol1 import alcohol1
from observations.r.birthdays import birthdays
from observations.r.births import births
from observations.r.births78 import births78
from observations.r.cps_85 import cps_85
from observations.r.cooling_water import cooling_water
from observations.r.countries import countries
from observations.r.dimes import dimes
from observations.r.galton2 import galton2
from observations.r.gestation import gestation
from observations.r.goose_permits import goose_permits
from observations.r.help_full import help_full
from observations.r.help_miss import help_miss
from observations.r.help_rct import help_rct
from observations.r.heat_x import heat_x
from observations.r.kids_feet import kids_feet
from observations.r.marriage import marriage
from observations.r.mites import mites
from observations.r.rail_trail import rail_trail
from observations.r.riders import riders
from observations.r.sat_state import sat_state
from observations.r.saratoga_houses import saratoga_houses
from observations.r.snow_gr import snow_gr
from observations.r.swim_records import swim_records
from observations.r.ten_mile_race import ten_mile_race
from observations.r.utilities import utilities
from observations.r.utilities2 import utilities2
from observations.r.whickham import whickham
from observations.r.auto import auto
from observations.r.caravan import caravan
from observations.r.carseats import carseats
from observations.r.college import college
from observations.r.default import default
from observations.r.oj import oj
from observations.r.portfolio import portfolio
from observations.r.smarket import smarket
from observations.r.wage import wage
from observations.r.weekly import weekly
from observations.r.alfalfa import alfalfa
from observations.r.archery_data import archery_data
from observations.r.auto_pollution import auto_pollution
from observations.r.backpack import backpack
from observations.r.baseball_times import baseball_times
from observations.r.bee_stings import bee_stings
from observations.r.bird_nest import bird_nest
from observations.r.blood1 import blood1
from observations.r.blue_jays import blue_jays
from observations.r.british_unions import british_unions
from observations.r.cafe import cafe
from observations.r.calcium_bp import calcium_bp
from observations.r.cancer_survival import cancer_survival
from observations.r.caterpillars import caterpillars
from observations.r.cereal import cereal
from observations.r.chemo_thc import chemo_thc
from observations.r.child_speaks import child_speaks
from observations.r.cloud_seeding import cloud_seeding
from observations.r.cloud_seeding2 import cloud_seeding2
from observations.r.cracker_fiber import cracker_fiber
from observations.r.cuckoo import cuckoo
from observations.r.day1_survey import day1_survey
from observations.r.diamonds import diamonds
from observations.r.diamonds2 import diamonds2
from observations.r.election08 import election08
from observations.r.ethanol1 import ethanol1
from observations.r.fgb_y_distance import fgb_y_distance
from observations.r.fantasy_baseball import fantasy_baseball
from observations.r.fertility import fertility
from observations.r.film import film
from observations.r.final_four_izzo import final_four_izzo
from observations.r.final_four_long import final_four_long
from observations.r.final_four_short import final_four_short
from observations.r.fingers import fingers
from observations.r.first_year_gpa import first_year_gpa
from observations.r.fish_eggs import fish_eggs
from observations.r.flight_response import flight_response
from observations.r.fluorescence import fluorescence
from observations.r.fruit_flies import fruit_flies
from observations.r.goldenrod import goldenrod
from observations.r.grocery import grocery
from observations.r.gunnels import gunnels
from observations.r.hawk_tail import hawk_tail
from observations.r.hawk_tail2 import hawk_tail2
from observations.r.hawks import hawks
from observations.r.hearing_test import hearing_test
from observations.r.high_peaks import high_peaks
from observations.r.hoops import hoops
from observations.r.horse_prices import horse_prices
from observations.r.houses import houses
from observations.r.icu import icu
from observations.r.infant_mortality import infant_mortality
from observations.r.insurance_vote import insurance_vote
from observations.r.jurors import jurors
from observations.r.kids198 import kids198
from observations.r.leaf_hoppers import leaf_hoppers
from observations.r.leukemia1 import leukemia1
from observations.r.long_jump_olympics import long_jump_olympics
from observations.r.lost_letter import lost_letter
from observations.r.mlb_2007_standings import mlb_2007_standings
from observations.r.marathon import marathon
from observations.r.markets import markets
from observations.r.math_enrollment import math_enrollment
from observations.r.math_placement import math_placement
from observations.r.med_gpa import med_gpa
from observations.r.mental_health import mental_health
from observations.r.metabolic_rate import metabolic_rate
from observations.r.metro_health83 import metro_health83
from observations.r.milgram import milgram
from observations.r.moth_eggs import moth_eggs
from observations.r.n_cbirths import n_cbirths
from observations.r.n_f_l2007_standings import n_f_l2007_standings
from observations.r.nursing import nursing
from observations.r.olives import olives
from observations.r.orings1 import orings1
from observations.r.overdrawn import overdrawn
from observations.r.palm_beach import palm_beach
from observations.r.pedometer import pedometer
from observations.r.perch import perch
from observations.r.pig_feed import pig_feed
from observations.r.pines import pines
from observations.r.political import political
from observations.r.pollster08 import pollster08
from observations.r.popcorn import popcorn
from observations.r.porsche_jaguar import porsche_jaguar
from observations.r.porsche_price import porsche_price
from observations.r.pulse import pulse
from observations.r.putts1 import putts1
from observations.r.putts2 import putts2
from observations.r.religion_gdp import religion_gdp
from observations.r.retirement import retirement
from observations.r.river_elements import river_elements
from observations.r.river_iron import river_iron
from observations.r.sat_gpa import sat_gpa
from observations.r.sample_fg import sample_fg
from observations.r.sandwich_ants import sandwich_ants
from observations.r.sea_slugs import sea_slugs
from observations.r.sparrows import sparrows
from observations.r.species_area import species_area
from observations.r.speed import speed
from observations.r.swahili import swahili
from observations.r.tms import tms
from observations.r.text_prices import text_prices
from observations.r.three_cars import three_cars
from observations.r.tip_joke import tip_joke
from observations.r.tomlinson_rush import tomlinson_rush
from observations.r.twins_lungs import twins_lungs
from observations.r.us_stamps import us_stamps
from observations.r.volts import volts
from observations.r.walking_babies import walking_babies
from observations.r.wght_loss_incentive import wght_loss_incentive
from observations.r.wght_loss_incentive4 import wght_loss_incentive4
from observations.r.wght_loss_incentive7 import wght_loss_incentive7
from observations.r.word_memory import word_memory
from observations.r.youth_risk2007 import youth_risk2007
from observations.r.youth_risk2009 import youth_risk2009
from observations.r.indian_irish import indian_irish
from observations.r.mendel_abc import mendel_abc
from observations.r.chain import chain
from observations.r.nlsy_v import nlsy_v
from observations.r.ced_data import ced_data
from observations.r.boundsdata import boundsdata
from observations.r.framing import framing
from observations.r.school import school
from observations.r.student import student
from observations.r.admnrev import admnrev
from observations.r.airfare import airfare
from observations.r.apple import apple
from observations.r.athlet1 import athlet1
from observations.r.athlet2 import athlet2
from observations.r.attend import attend
from observations.r.audit import audit
from observations.r.barium import barium
from observations.r.beauty import beauty
from observations.r.benefits1 import benefits1
from observations.r.beveridge import beveridge
from observations.r.big9salary import big9salary
from observations.r.bwght import bwght
from observations.r.bwght2 import bwght2
from observations.r.campus import campus
from observations.r.card import card
from observations.r.ceosal1 import ceosal1
from observations.r.ceosal2 import ceosal2
from observations.r.charity import charity
from observations.r.consump import consump
from observations.r.corn import corn
from observations.r.cps78_85 import cps78_85
from observations.r.cps91 import cps91
from observations.r.crime1 import crime1
from observations.r.crime2 import crime2
from observations.r.crime3 import crime3
from observations.r.crime4 import crime4
from observations.r.discrim import discrim
from observations.r.driving import driving
from observations.r.earns import earns
from observations.r.elem94_95 import elem94_95
from observations.r.engin import engin
from observations.r.expendshares import expendshares
from observations.r.ezanders import ezanders
from observations.r.ezunem import ezunem
from observations.r.fair1 import fair1
from observations.r.fertil1 import fertil1
from observations.r.fertil2 import fertil2
from observations.r.fertil3 import fertil3
from observations.r.fish import fish
from observations.r.fringe import fringe
from observations.r.gpa1 import gpa1
from observations.r.gpa2 import gpa2
from observations.r.gpa3 import gpa3
from observations.r.happiness import happiness
from observations.r.hprice1 import hprice1
from observations.r.hprice2 import hprice2
from observations.r.hprice3 import hprice3
from observations.r.hseinv import hseinv
from observations.r.htv import htv
from observations.r.infmrt import infmrt
from observations.r.injury import injury
from observations.r.intdef import intdef
from observations.r.intqrt import intqrt
from observations.r.inven import inven
from observations.r.jtrain import jtrain
from observations.r.jtrain2 import jtrain2
from observations.r.jtrain3 import jtrain3
from observations.r.kielmc import kielmc
from observations.r.lawsch85 import lawsch85
from observations.r.loanapp import loanapp
from observations.r.lowbrth import lowbrth
from observations.r.mathpnl import mathpnl
from observations.r.meap00_01 import meap00_01
from observations.r.meap01 import meap01
from observations.r.meap93 import meap93
from observations.r.minwage import minwage
from observations.r.mlb1 import mlb1
from observations.r.mroz2 import mroz2
from observations.r.murder import murder
from observations.r.nbasal import nbasal
from observations.r.nyse import nyse
from observations.r.okun import okun
from observations.r.openness import openness
from observations.r.phillips import phillips
from observations.r.pntsprd import pntsprd
from observations.r.prison import prison
from observations.r.prminwge import prminwge
from observations.r.rdchem import rdchem
from observations.r.rdtelec import rdtelec
from observations.r.recid import recid
from observations.r.rental import rental
from observations.r.company_return import company_return
from observations.r.saving import saving
from observations.r.sleep75 import sleep75
from observations.r.slp75_81 import slp75_81
from observations.r.smoke import smoke
from observations.r.traffic1 import traffic1
from observations.r.traffic2 import traffic2
from observations.r.twoyear import twoyear
from observations.r.volat import volat
from observations.r.vote1 import vote1
from observations.r.vote2 import vote2
from observations.r.voucher import voucher
from observations.r.wage1 import wage1
from observations.r.wage2 import wage2
from observations.r.wagepan import wagepan
from observations.r.wageprc import wageprc
from observations.r.wine import wine


def remove_undocumented(module_name, allowed_exception_list=None):
  """Removes symbols in a module that are not referenced by a docstring.

  Args:
    module_name: the name of the module (usually `__name__`).
    allowed_exception_list: a list of names that should not be removed.

  Returns:
    None
  """
  import sys as _sys
  current_symbols = set(dir(_sys.modules[module_name]))
  should_have = allowed_exception_list or []
  extra_symbols = current_symbols - set(should_have)
  target_module = _sys.modules[module_name]
  for extra_symbol in extra_symbols:
    # Skip over __file__, etc. Also preserves internal symbols.
    if extra_symbol.startswith('_'):
      continue
    fully_qualified_name = module_name + '.' + extra_symbol
    delattr(target_module, extra_symbol)


# Export modules and constants.
_allowed_symbols = [
    'air_passengers',
    'bj_sales',
    'bod',
    'co2',
    'formaldehyde',
    'hair_eye_color',
    'insect_sprays',
    'johnson_johnson',
    'lake_huron',
    'life_cycle_savings',
    'nile',
    'orchard_sprays',
    'plant_growth',
    'puromycin',
    'titanic',
    'tooth_growth',
    'ucb_admissions',
    'uk_driver_deaths',
    'uk_gas',
    'us_acc_deaths',
    'us_arrests',
    'us_judge_ratings',
    'us_personal_expend',
    'va_deaths',
    'www_usage',
    'world_phones',
    'airmiles',
    'airquality',
    'anscombe',
    'attenu',
    'attitude',
    'austres',
    'cars',
    'chickwts',
    'co2_1',
    'crimtab',
    'discoveries',
    'esoph',
    'euro',
    'faithful',
    'freeny',
    'infert',
    'iris',
    'islands',
    'lh',
    'longley',
    'lynx',
    'morley',
    'mtcars',
    'nhtemp',
    'nottem',
    'npk',
    'occupational_status',
    'precip',
    'presidents',
    'pressure',
    'quakes',
    'randu',
    'rivers',
    'rock',
    'sleep',
    'stackloss',
    'sunspot_month',
    'sunspot_year',
    'sunspots',
    'swiss',
    'treering',
    'trees',
    'uspop',
    'volcano',
    'warpbreaks',
    'women',
    'acme',
    'aids',
    'aircondit',
    'aircondit7',
    'amis',
    'aml',
    'bigcity',
    'brambles',
    'breslow',
    'calcium',
    'cane',
    'capability',
    'cats_m',
    'cav',
    'cd4',
    'channing',
    'city',
    'claridge',
    'cloth',
    'co_transfer',
    'coal',
    'darwin',
    'dogs',
    'downs_bc',
    'ducks',
    'fir',
    'frets',
    'grav',
    'gravity',
    'hirose',
    'islay',
    'manaus',
    'melanoma',
    'motor',
    'neuro',
    'nitrofen',
    'nodal',
    'nuclear',
    'paulsen',
    'poisons',
    'polar',
    'remission',
    'salinity',
    'survival',
    'tau',
    'tuna',
    'urine',
    'wool',
    'acf1',
    'cars93_summary',
    'lottario',
    'manitoba_lakes',
    'sp500_w90',
    'sp500_close',
    'ais',
    'allbacks',
    'anesthetic',
    'ant111b',
    'antigua',
    'appletaste',
    'aulatlong',
    'austpop',
    'biomass',
    'bomregions',
    'bomregions2011',
    'bomregions2012',
    'bomsoi',
    'bomsoi2001',
    'carprice',
    'cerealsugar',
    'cfseal',
    'cities',
    'codling',
    'cottonworkers',
    'cps1',
    'cps2',
    'cps3',
    'cricketer',
    'cuckoohosts',
    'cuckoos',
    'dengue',
    'dewpoint',
    'droughts',
    'edc_co2',
    'edc_t',
    'elastic1',
    'elastic2',
    'elasticband',
    'fossilfuel',
    'fossum',
    'frogs',
    'frostedflakes',
    'fruitohms',
    'gaba',
    'geophones',
    'grog',
    'head_injury',
    'hills',
    'hills2000',
    'hotspots',
    'hotspots2006',
    'houseprices',
    'humanpower1',
    'humanpower2',
    'hurric_named',
    'intersalt',
    'ironslag',
    'jobs',
    'kiwishade',
    'leafshape',
    'leafshape17',
    'leaftemp',
    'leaftemp_all',
    'litters',
    'lung',
    'measles',
    'med_expenses',
    'mifem',
    'mignonette',
    'milk',
    'modelcars',
    'monica',
    'moths',
    'nass_cds',
    'nasshead',
    'nihills',
    'nsw74demo',
    'nsw74psid1',
    'nsw74psid3',
    'nsw74psid_a',
    'nswdemo',
    'nswpsid1',
    'oddbooks',
    'orings',
    'pair65',
    'possum',
    'possumsites',
    'primates',
    'progression',
    'psid1',
    'psid2',
    'psid3',
    'races2000',
    'rainforest',
    'rareplants',
    'rice',
    'rock_art',
    'roller',
    'science',
    'seedrates',
    'socsupport',
    'softbacks',
    'sorption',
    'spam7',
    'st_vincent',
    'sugar',
    'tinting',
    'tomato',
    'toycars',
    'vince111b',
    'vlt',
    'wages1833',
    'world_records',
    'fars',
    'air_accs',
    'cvalues',
    'fars2007',
    'fars2008',
    'german',
    'loti',
    'alloauto',
    'allograft',
    'azt',
    'baboon',
    'bcdeter',
    'bfeed',
    'bmt',
    'bnct',
    'btrial',
    'burn',
    'drug6mp',
    'drughiv',
    'hodg',
    'kidrecurr',
    'kidtran',
    'larynx',
    'pneumon',
    'psych',
    'std',
    'stddiag',
    'tongue',
    'twins',
    'animals2',
    'crohn_d',
    'n_ox_emissions',
    'siegels_ex',
    'aircraft',
    'airmay',
    'alcohol',
    'ambient_noxch',
    'biomass_till',
    'bushfire',
    'carrots',
    'cloud',
    'coleman',
    'condroz',
    'cushny',
    'delivery',
    'education',
    'epilepsy',
    'ex_am',
    'foodstamp',
    'hbk',
    'heart',
    'kootenay',
    'lactic',
    'pension',
    'phosphor',
    'pilot',
    'possum_div',
    'pulpfiber',
    'radar_image',
    'stars_cyg',
    'telef',
    'toxicity',
    'vaso',
    'wagner_growth',
    'wood',
    'ams_survey',
    'adler',
    'angell',
    'us_public_school',
    'baumann',
    'bfox',
    'blackmore',
    'burt',
    'can_pop',
    'chile',
    'chirot',
    'cowles',
    'davis',
    'davis_thin',
    'depredations',
    'duncan',
    'ericksen',
    'florida',
    'freedman',
    'friendly',
    'ginzberg',
    'greene',
    'guyer',
    'hartnagel',
    'highway1',
    'kostecki_dillon',
    'leinhardt',
    'lo_bd',
    'mandel',
    'migration',
    'moore',
    'mroz',
    'o_brien_kaiser',
    'ornstein',
    'pottery',
    'prestige',
    'quartet',
    'robey',
    'slid',
    'sahlins',
    'salaries',
    'soils',
    'states',
    'transact',
    'gdp_infant_mortality',
    'us_pop',
    'vocab',
    'weight_loss',
    'womenlf',
    'wong',
    'wool1',
    'agriculture',
    'animals',
    'chor_sub',
    'flower',
    'plant_traits',
    'pluton',
    'ruspini',
    'votes_repub',
    'xclara',
    'affairs',
    'azcabgptca',
    'azdrg112',
    'azpro',
    'azprocedure',
    'badhealth',
    'fasttrakg',
    'fishing',
    'lbw',
    'lbwgrp',
    'loomis',
    'mdvis',
    'medpar',
    'nuts',
    'rwm',
    'rwm1984',
    'rwm5yr',
    'smoking',
    'titanicgrp',
    'accident',
    'airline',
    'airq',
    'benefits',
    'bids',
    'budget_food',
    'budget_italy',
    'budget_uk',
    'bwages',
    'cp_sch3',
    'cran_packages',
    'capm',
    'car',
    'caschool',
    'catsup',
    'cigar',
    'cigarette',
    'clothing',
    'computers',
    'cracker',
    'crime',
    'dm',
    'diamond',
    'doctor',
    'doctor_aus',
    'doctor_contacts',
    'earnings',
    'electricity',
    'fair',
    'fatality',
    'fishing1',
    'forward',
    'friend_foe',
    'garch',
    'gasoline',
    'griliches',
    'grunfeld',
    'hc_choice_california',
    'hhs_cybsec_breaches',
    'hi_hours_worked',
    'hdma',
    'heating',
    'hedonic',
    'hmda',
    'housing',
    'icecream',
    'journals',
    'kakadu',
    'ketchup',
    'klein',
    'labor_supply',
    'labour',
    'mcas',
    'males',
    'mathlevel',
    'med_exp',
    'metal',
    'mode',
    'mode_choice',
    'mofa',
    'mroz1',
    'mun_exp',
    'natural_park',
    'nerlove',
    'ofp',
    'oil',
    'psid',
    'participation',
    'patents_hgh',
    'patents_rd',
    'pound',
    'produc',
    'ret_school',
    'sp500',
    'schooling',
    'somerville',
    'star',
    'strike',
    'strike_dur',
    'strike_nb',
    'tobacco',
    'train',
    'transp_eq',
    'treatment',
    'tuna1',
    'us_finance_industry',
    'us_gdp_presidents',
    'us_classified_docs',
    'us_state_abbrev',
    'us_tax_words',
    'unemp_dur',
    'unemployment',
    'university',
    'vietnam_h',
    'vietnam_i',
    'wages',
    'wages1',
    'workinghours',
    'yen',
    'yogurt',
    'banking_crises',
    'breaches',
    'terr_incidents',
    'income_inequality',
    'nkill_by_country_yr',
    'non_english_names',
    'political_knowledge',
    'terrorism',
    'parkinsons',
    'aldh2',
    'apoeapoc',
    'cf',
    'crohn',
    'fa',
    'fsnps',
    'hla',
    'hr1420',
    'l51',
    'lukas',
    'mao',
    'meyer',
    'mfblong',
    'mhtdata',
    'nep499',
    'luv_colours',
    'arbuthnot',
    'armada',
    'bowley',
    'cavendish',
    'chest_sizes',
    'cholera',
    'cushny_peebles',
    'cushny_peebles_n',
    'dactyl',
    'drinks_wages',
    'fingerprints',
    'galton',
    'galton_families',
    'guerry',
    'halley_life_table',
    'jevons',
    'langren_all',
    'langren1644',
    'macdonell',
    'macdonell_df',
    'michelson',
    'michelson_sets',
    'minard_cities',
    'minard_temp',
    'minard_troops',
    'nightingale',
    'old_maps',
    'pearson_lee',
    'polio_trials',
    'prostitutes',
    'pyx',
    'quarrels',
    'snow_dates',
    'snow_deaths',
    'snow_deaths2',
    'snow_pumps',
    'snow_streets',
    'wheat',
    'wheat_monarchs',
    'yeast',
    'yeast_d_mat',
    'zea_mays',
    'barley',
    'environmental',
    'ethanol',
    'melanoma',
    'singer',
    'aids2',
    'animals1',
    'boston',
    'cars93',
    'cushings',
    'ddt_kale',
    'gag_urine',
    'insurance',
    'melanoma1',
    'ome_children',
    'pima_te',
    'pima_tr',
    'pima_tr2',
    'rabbit',
    'rubber',
    'sitka',
    'sitka89',
    'skye',
    'traffic',
    'us_cereal',
    'us_crime',
    'va_lung_cancer',
    'abbey',
    'accdeaths',
    'anorexia',
    'bacteria',
    'beav1',
    'beav2',
    'biopsy',
    'birthwt',
    'cabbages',
    'caith',
    'cats',
    'cement',
    'chem',
    'coop',
    'cpus',
    'crabs',
    'deaths',
    'drivers',
    'eagles',
    'epil',
    'farms',
    'fgl',
    'forbes',
    'galaxies',
    'gehan',
    'genotype',
    'geyser',
    'gilgais',
    'housing1',
    'immer',
    'leuk',
    'mammals',
    'mcycle',
    'menarche',
    'michelson1',
    'minn38',
    'motors',
    'muscle',
    'newcomb',
    'nlschools',
    'npr1',
    'oats',
    'painters',
    'petrol',
    'quine',
    'road',
    'rotifer',
    'ships',
    'shrimp',
    'shuttle',
    'snails',
    'steam',
    'stormer',
    'survey',
    'synth_te',
    'synth_tr',
    'topo',
    'waders',
    'whiteside',
    'wtloss',
    'empl_uk',
    'grunfeld1',
    'males1',
    'parity',
    'rice_farms',
    'snmesp',
    'sum_hes',
    'baseball',
    'aus_election_polling',
    'australian_elections',
    'efron_morris',
    'rock_the_vote',
    'uk_house_of_commons',
    'absentee',
    'admit',
    'bio_chemists',
    'ca2006',
    'iraq_vote',
    'political_info',
    'president_elections',
    'prussian',
    'union_density',
    'vote92',
    'french_fries',
    'tips',
    'car_test_frame',
    'car90',
    'cu_summary',
    'kyphosis',
    'solder',
    'stagec',
    'public_schools',
    'bollen',
    'cnes',
    'klein1',
    'mental_tests',
    'bladder',
    'cancer',
    'cgd',
    'colon',
    'flchain',
    'genfan',
    'kidney',
    'leukemia',
    'logan',
    'lung',
    'mgus',
    'mgus2',
    'myeloid',
    'nwtco',
    'ovarian',
    'pbc',
    'rats',
    'retinopathy',
    'rh_dnase',
    'stanford2',
    'tobin',
    'transplant',
    'veteran',
    'arthritis',
    'baseball1',
    'broken_marriage',
    'bundesliga',
    'bundestag2005',
    'butterfly',
    'coal_miners',
    'danish_welfare',
    'employment',
    'federalist',
    'hitters',
    'horse_kicks',
    'hospital',
    'job_satisfaction',
    'joint_sports',
    'lifeboats',
    'non_response',
    'ovary_cancer',
    'pre_sex',
    'punishment',
    'rep_vict',
    'saxony',
    'sexual_fun',
    'space_shuttle',
    'suicide',
    'trucks',
    'uk_soccer',
    'visual_acuity',
    'von_bort',
    'weldon_dice',
    'women_queue',
    'p_erisk',
    'supreme_court',
    'weimar',
    'approval',
    'bivariate',
    'coalition',
    'coalition2',
    'eidat',
    'free1',
    'free2',
    'friendship',
    'grunfeld2',
    'hoff',
    'homerun',
    'immi1',
    'immi2',
    'immi3',
    'immi4',
    'immi5',
    'immigration',
    'klein2',
    'kmenta2',
    'macro',
    'mexico',
    'mid',
    'newpainters',
    'sanction',
    'seatshare',
    'sna_ex',
    'turnout',
    'voteincome',
    'bcg_vaccine',
    'bthe_b',
    'cygob1',
    'forbes2000',
    'ghq',
    'lanza',
    'agefat',
    'aspirin',
    'birthdeathrates',
    'bladdercancer',
    'clouds',
    'foster',
    'heptathlon',
    'mastectomy',
    'meteo',
    'orallesions',
    'phosphate',
    'pistonrings',
    'planets',
    'plasma',
    'polyps',
    'polyps3',
    'pottery1',
    'rearrests',
    'respiratory',
    'roomwidth',
    'schizophrenia',
    'schizophrenia2',
    'schooldays',
    'skulls',
    'students',
    'suicides',
    'toothpaste',
    'voting',
    'water',
    'watervoles',
    'waves',
    'weightgain',
    'womensrole',
    'bechtoldt',
    'bechtoldt_1',
    'bechtoldt_2',
    'dwyer',
    'gleser',
    'gorsuch',
    'harman_5',
    'harman_8',
    'harman_political',
    'holzinger',
    'holzinger_9',
    'reise',
    'schmid',
    'schutz',
    'thurstone',
    'thurstone_33',
    'tucker',
    'ability',
    'affect',
    'bfi',
    'bfi_dictionary',
    'blot',
    'burt1',
    'cattell',
    'cities1',
    'cubits',
    'epi',
    'epi_bfi',
    'epi_dictionary',
    'galton1',
    'heights',
    'income',
    'iqitems',
    'msq',
    'neo',
    'peas',
    'sat_act',
    'within_between',
    'bosco',
    'cobar_ore',
    'mammals1',
    'barro',
    'engel',
    'gasprice',
    'uis',
    'dietox',
    'koch',
    'ohio',
    'respdis',
    'seizure',
    'spruce',
    'liver',
    'nidd',
    'portpirie',
    'rain',
    'summer',
    'wavesurge',
    'winter',
    'arthritis1',
    'bmw',
    'danish',
    'nidd_annual',
    'nidd_thresh',
    'siemens',
    'sp_raw',
    'spto87',
    'arabidopsis',
    'dyestuff',
    'dyestuff2',
    'pastes',
    'penicillin',
    'verb_agg',
    'cake',
    'cbpp',
    'grouseticks',
    'sleepstudy',
    'alcohol1',
    'birthdays',
    'births',
    'births78',
    'cps_85',
    'cooling_water',
    'countries',
    'dimes',
    'galton2',
    'gestation',
    'goose_permits',
    'help_full',
    'help_miss',
    'help_rct',
    'heat_x',
    'kids_feet',
    'marriage',
    'mites',
    'rail_trail',
    'riders',
    'sat_state',
    'saratoga_houses',
    'snow_gr',
    'swim_records',
    'ten_mile_race',
    'utilities',
    'utilities2',
    'whickham',
    'auto',
    'caravan',
    'carseats',
    'college',
    'default',
    'oj',
    'portfolio',
    'smarket',
    'wage',
    'weekly',
    'alfalfa',
    'archery_data',
    'auto_pollution',
    'backpack',
    'baseball_times',
    'bee_stings',
    'bird_nest',
    'blood1',
    'blue_jays',
    'british_unions',
    'cafe',
    'calcium_bp',
    'cancer_survival',
    'caterpillars',
    'cereal',
    'chemo_thc',
    'child_speaks',
    'cloud_seeding',
    'cloud_seeding2',
    'cracker_fiber',
    'cuckoo',
    'day1_survey',
    'diamonds',
    'diamonds2',
    'election08',
    'ethanol1',
    'fgb_y_distance',
    'fantasy_baseball',
    'fertility',
    'film',
    'final_four_izzo',
    'final_four_long',
    'final_four_short',
    'fingers',
    'first_year_gpa',
    'fish_eggs',
    'flight_response',
    'fluorescence',
    'fruit_flies',
    'goldenrod',
    'grocery',
    'gunnels',
    'hawk_tail',
    'hawk_tail2',
    'hawks',
    'hearing_test',
    'high_peaks',
    'hoops',
    'horse_prices',
    'houses',
    'icu',
    'infant_mortality',
    'insurance_vote',
    'jurors',
    'kids198',
    'leaf_hoppers',
    'leukemia1',
    'long_jump_olympics',
    'lost_letter',
    'mlb_2007_standings',
    'marathon',
    'markets',
    'math_enrollment',
    'math_placement',
    'med_gpa',
    'mental_health',
    'metabolic_rate',
    'metro_health83',
    'milgram',
    'moth_eggs',
    'n_cbirths',
    'n_f_l2007_standings',
    'nursing',
    'olives',
    'orings1',
    'overdrawn',
    'palm_beach',
    'pedometer',
    'perch',
    'pig_feed',
    'pines',
    'political',
    'pollster08',
    'popcorn',
    'porsche_jaguar',
    'porsche_price',
    'pulse',
    'putts1',
    'putts2',
    'religion_gdp',
    'retirement',
    'river_elements',
    'river_iron',
    'sat_gpa',
    'sample_fg',
    'sandwich_ants',
    'sea_slugs',
    'sparrows',
    'species_area',
    'speed',
    'swahili',
    'tms',
    'text_prices',
    'three_cars',
    'tip_joke',
    'tomlinson_rush',
    'twins_lungs',
    'us_stamps',
    'volts',
    'walking_babies',
    'wght_loss_incentive',
    'wght_loss_incentive4',
    'wght_loss_incentive7',
    'word_memory',
    'youth_risk2007',
    'youth_risk2009',
    'indian_irish',
    'mendel_abc',
    'chain',
    'nlsy_v',
    'ced_data',
    'boundsdata',
    'framing',
    'school',
    'student',
    'admnrev',
    'airfare',
    'apple',
    'athlet1',
    'athlet2',
    'attend',
    'audit',
    'barium',
    'beauty',
    'benefits1',
    'beveridge',
    'big9salary',
    'bwght',
    'bwght2',
    'campus',
    'card',
    'ceosal1',
    'ceosal2',
    'charity',
    'consump',
    'corn',
    'cps78_85',
    'cps91',
    'crime1',
    'crime2',
    'crime3',
    'crime4',
    'discrim',
    'driving',
    'earns',
    'elem94_95',
    'engin',
    'expendshares',
    'ezanders',
    'ezunem',
    'fair1',
    'fertil1',
    'fertil2',
    'fertil3',
    'fish',
    'fringe',
    'gpa1',
    'gpa2',
    'gpa3',
    'happiness',
    'hprice1',
    'hprice2',
    'hprice3',
    'hseinv',
    'htv',
    'infmrt',
    'injury',
    'intdef',
    'intqrt',
    'inven',
    'jtrain',
    'jtrain2',
    'jtrain3',
    'kielmc',
    'lawsch85',
    'loanapp',
    'lowbrth',
    'mathpnl',
    'meap00_01',
    'meap01',
    'meap93',
    'minwage',
    'mlb1',
    'mroz2',
    'murder',
    'nbasal',
    'nyse',
    'okun',
    'openness',
    'phillips',
    'pntsprd',
    'prison',
    'prminwge',
    'rdchem',
    'rdtelec',
    'recid',
    'rental',
    'company_return',
    'saving',
    'sleep75',
    'slp75_81',
    'smoke',
    'traffic1',
    'traffic2',
    'twoyear',
    'volat',
    'vote1',
    'vote2',
    'voucher',
    'wage1',
    'wage2',
    'wagepan',
    'wageprc',
    'wine'

]

# Remove all extra symbols that don't have a docstring or are not explicitly
# referenced in the whitelist.
remove_undocumented(__name__, _allowed_symbols)
