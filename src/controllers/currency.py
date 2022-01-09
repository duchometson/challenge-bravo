from flask import Flask, request
from flask_restx import Api, Resource

from controllers.validator.requestvalidator import RequestValidator
from server.server import *
from services.currencyservice import CurrencyService
from exceptions.apiexceptions import DatabaseException, InvalidParametersException, InvalidCurrenciesException
from models.responsemodel import *


@server.route('/currency', methods=['GET'])
def getCurrency(self):
    try:
        request_model = RequestValidator.validateCurrencyGetRequestArgs(request.args)
        currency_json = CurrencyService.getCurrency(request_model.name)
    except (InvalidParametersException, InvalidCurrenciesException) as e:
        return ErrorResponse.create(e.message,e.statusCode)

    return SuccessResponse.create(request_model.name,
                                    currency_json)

@server.route('/currency', methods=['PUT'])
def putCurrency(self):
    try:
        request_model = RequestValidator.validateCurrencyPutRequestArgs(request.args)
        CurrencyService.saveCurrency(request_model.name,request_model.value)
    except (InvalidParametersException, DatabaseException) as e:
        return ErrorResponse.create(e.message,e.statusCode)

    return SuccessResponse.create(request_model.name,{})

@server.route('/currency', methods=['DELETE'])
def deleteCurrency(self):
    try:
        request_model = RequestValidator.validateCurrencyDeleteRequestArgs(request.args)
        CurrencyService.removeCurrency(request_model.name)
    except (InvalidParametersException, DatabaseException) as e:
        return ErrorResponse.create(e.message,e.statusCode)

    return SuccessResponse.create(request_model.name,{})
